#standard ds imports
import pandas as pd
import numpy as np

#imports
import os
import datetime

from env import username, host, password



################################## Temperature by State Acquire Function ############################  

def wrangle_temp_by_state():
    '''
    Checks for a local cache of tsa_store_data.csv and if not present will run 
    the get_store_data() function which acquires data from Codeup's mysql server
    '''
    filename = 'GlobalLandTemperaturesByState.csv'
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
        
    return df
