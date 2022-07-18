# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:44:18 2022

@author: yale-winter
yalewinter.com
"""

import pandas as pd
from datetime import date, timedelta
from . commands import find_next_to_dos,find_to_do_progress,find_recent_progress
import os

def fix_dates_in_col(df, col_index, col_names):
    '''
    Formats dates in a collumn
    ----------
    Returns
    -------
    modified DataFrame

    '''
    try:
        ldf = df.tolist()
        for i in range(len(ldf)):
            ldf[i][col_index] = pd.to_datetime(df.iloc[i][col_index])
        df = pd.DataFrame(ldf, columns=col_names)  
    except:
        print('cant format dates')
    return df

def import_data_table(file_name, online, gsheet_mid_link, read_rows, col_names):
    '''
    Import timeline from .csv file
    
    Parameters
    ----------
    file_name : string
        File name including file extension
    online : bool
        Read online or local
    read_rows : number
        number of rows to read
    col_names : array of strings
        names of columns

    Returns
    -------
    DataFrame of the content or error string

    '''
    df = 'error importing data'
    if online:
        try:
            df = pd.read_csv('https://docs.google.com/spreadsheets/d/' + 
            gsheet_mid_link +
            '/export?gid=0&format=csv',nrows=read_rows, on_bad_lines='skip')
            print('loaded data table from google sheet online')
        except:
            print('error loading data table from google sheet online')
            online = False
            
    if online == False:
        try:
            __location__ = os.path.realpath(
                os.path.join(os.getcwd(), os.path.dirname(__file__)))
            sheet_url = os.path.join(__location__, file_name)  
            df = pd.read_csv(sheet_url,nrows=read_rows, on_bad_lines='skip')
            print('loaded data table from local .csv')
        except:
            print('error loading data from local .csv')
    
    # drop rows where at least 1 element is missing
    if type(df) == pd.DataFrame:
        df.dropna()

    return df

def start():
    '''
    Start up and display To-Do information
    '''
    import_online = False
    gsheet_mid_link = '___link_url_here____'
    col_names = ['To-Dos', 'Date Assigned', 'Date Complete', 'Priority']
    df = import_data_table('ToDos.csv', import_online, gsheet_mid_link, 1000, col_names)
    try:
        df = fix_dates_in_col(df, 1, col_names)
        df = fix_dates_in_col(df, 2, col_names)
        find_next_to_dos(df)
        prog = find_to_do_progress(df)
        find_recent_progress(df, prog)
    except:
        print('loading data error')
    return df
    
df = start()