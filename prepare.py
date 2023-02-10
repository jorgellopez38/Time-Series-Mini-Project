import numpy as np
import pandas as pd

#datetime utilities
from datetime import timedelta, datetime

import os
import acquire


################################## Temperature by State Prep Function ############################

def prep_temp():
    #change data type on Date
    df.dt = df.dt.astype('datetime64[ns]')
    #set the index to Date
    df = df.set_index('dt').sort_index()
    #rename columns
    df = df.rename(columns={'AverageTemperature':'average_temp', 
                            'AverageTemperatureUncertainty':'average_temp_uncertainty', 
                            'State':'state','Country':'country'})
    # rename index
    df.index.names = ['date']
    # fill nulls
    df = df.fillna(0)
    #create new colum for month
    df['month'] = df.index.month_name()
    #create new colum for weekday
    df['day_of_week'] = df.index.day_name()
    #create new column for year
    df['year'] = df.index.year

    return df


################################## Temperature by State Split Function ############################


def split_temp(df):
    train_len = int(0.6 * len(df))
    val_test_split = int(0.8 * len(df))
    train_len, val_test_split

    train = df.iloc[:train_len]
    val = df.iloc[train_len:val_test_split]
    test = df.iloc[val_test_split:]
    # Have function print datasets shape
    print(f'train -> {train.shape}')
    print(f'validate -> {val.shape}')
    print(f'test -> {test.shape}')
    
    return train, val, test 