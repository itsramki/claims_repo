from glob import glob
import etl
from code.filereadingmanager import Claimspecs
from code.databasemanager import ConnectMySQLServer




def test_filereadingmanager():
    
    c = Claimspecs()
    
    srcSpecPath = r"D:\claims\specs\claimsspec1.txt"
    pattern = r"D:\claims\data\claimsdata*.txt"
    testsrcFiles = glob(pattern)

    testspecs = c.get_Claimspecs(srcSpecPath)
    srcData = c.filename_validation_read (testsrcFiles, testspecs)

    assert not(testspecs.empty) # testing whether dataframe is empty
    assert not(srcData.empty) # testing whether srcfile has data

def test_databasemanager():

    d = ConnectMySQLServer('localhost', 'claims', 'guest', 'guest')

    eng = d.sqlalchemyengine()

    assert eng.connect()
