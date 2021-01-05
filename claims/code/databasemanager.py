from sqlalchemy import create_engine
import pymysql

class ConnectMySQLServer:

    """
    This class has parameters and methods related to connect to database
    """

    def __init__(self, server, DBName, username, password):
        
        self.server = server
        self.DBName = DBName
        self.username = username
        self.password = password

    def sqlalchemyengine(self):

        """Initiates sqlalchemy engine """

        db = 'SERVER=' + self.server + ';' \
             'UID=' + self.username + ';' \
             'PWD=' + self.password + ';' \
             'DATABASE=' + self.DBName + ';'

        conn_str = "mysql+pymysql://{}:{}@{}:3306/{}".format(self.username, self.password, self.server, self.DBName)
               
        return conn_str
        