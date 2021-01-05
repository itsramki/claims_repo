import pandas as pd
import datetime
import os

class Claimspecs:
    
    @staticmethod
    def get_Claimspecs(specfile):
        """ method to read the specfile """
        specdf = pd.read_csv(specfile)
 
        return specdf

    @staticmethod
    def filename_validation_read(srcfiles, specs):
       
        """ This module is to check if the source file has correct names as expected 
        if it has the correct name, it reads the same"""
        
        df = pd.DataFrame()
        widths = list(specs.width) #setting widths from spec file while reading the fixed width file
        cols = list(specs["field name"])
        
        for name in srcfiles:
            
            if name.endswith(".txt"):
                a = name.split("\\")[-1].split(".")[0].split("_", 1) #splitting the filename
                if a[0] == "claimsdata":
                    try:
                        datetime.datetime.strptime(a[1], '%Y_%m_%d')
                        df = df.append(pd.read_fwf(name, width = widths, header = None)) # reading the file
                    except ValueError:
                        pass
        df.columns = cols
        return df.reset_index(drop = True)









