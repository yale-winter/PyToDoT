# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:44:18 2022

@author: yale-winter
yalewinter.com
"""
import os
import pandas as pd
from . commands import find_next_to_dos, find_to_do_progress, find_recent_progress, set_ldf
def fix_dates_in_col(j, col_index, col_names):
    '''
    Formats dates in a collumn
    ----------
    Returns
    -------
    modified DataFrame

    '''
    ldf2 = j.values.tolist()
    for i in range(1, len(ldf2)):
        ldf2[i][col_index] = pd.to_datetime(j.iloc[i][col_index])
    j = pd.DataFrame(ldf2, columns=col_names)
    return j
def import_data_table(file_name, read_rows):
    '''
    Import timeline from .csv file
    Parameters
    ----------
    file_name : string
        File name including file extension
    read_rows : number
        number of rows to read
    col_names : array of strings
        names of columns
    Returns
    -------
    DataFrame of the content or None
    '''
    j = None
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    sheet_url = os.path.join(__location__, file_name)
    j = pd.read_csv(sheet_url, nrows=read_rows, on_bad_lines='skip')
    print('loaded data table from local .csv')
    # drop rows where at least 1 element is missing
    if isinstance(j, pd.DataFrame):
        j.dropna()
    return j
def start():
    '''
    Start up and display To-Do information
    '''
    col_names = ['To-Dos', 'Date Assigned', 'Date Complete', 'Priority']
    j = import_data_table('ToDos.csv', 1000)
    j = fix_dates_in_col(j, 1, col_names)
    j = fix_dates_in_col(j, 2, col_names)
    find_next_to_dos(j)
    prog = find_to_do_progress(j)
    find_recent_progress(j, prog)
    return j
j = start()
set_ldf(j)
