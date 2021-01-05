from glob import glob
import pandas as pd
from mysql.connector import connect, Error
from code.filereadingmanager import Claimspecs
from code.databasemanager import ConnectMySQLServer
from sqlalchemy import create_engine, exc


def main():
    specFilePath = r'D:\claims\specs\claimsspec1.txt' # we can use config file to specify the paths
    specs = Claimspecs.get_Claimspecs(specFilePath)  # Reading claims spec file

    pattern = r'D:\claims\data\claimsdata*.txt'
    lst_srcFiles = glob(pattern) # getting all the sourcefiles with name claims*.txt

    srcdf = Claimspecs.filename_validation_read(lst_srcFiles, specs) # Reading all eligible files into a dataframe

        
    mySqlServer = ConnectMySQLServer('localhost', 'claims', 'guest', 'guest') #This is not good way of adding password, we use environmental variables in actual programme
   
    try:
        connectionstring = mySqlServer.sqlalchemyengine()
        engine = create_engine(connectionstring)
        conn = engine.connect()
        srcdf.to_sql('claims', con = conn, if_exists = 'append', index = False)
        status = "file loaded in database"
        conn.close()
    except exc.SQLAlchemyError:
        status = "Not connected to database, please check connection details"
    
    return status


if __name__ == "__main__":
    
    file_load_status = main()

    print(file_load_status)
