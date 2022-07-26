# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:51:30 2022

@author: yale-winter
yalewinter.com
"""
import pandas as pd
from datetime import date, timedelta


def to_do(x, df = None):
    '''
    Print the to-do description from row id
    '''
    # use local DF if calling command with no params
    global lDF
    if df is None:
        df = lDF
    print('\nTop To-Do:')
    print('>>>',df.iloc[x][0])

def find_recent_progress(df, prog):  
    '''
    Show information regarding to-do progress in last 30 days
    '''
    days_before = pd.Timestamp((date.today()-timedelta(days=30)))
    df3 = df.iloc[0,1]
    delta = pd.Timestamp(date.today()) - pd.Timestamp(df3)
    print('Days since tracking:',delta.days)
    print('Average To-Dos completed in 30 days:', int(prog[0] / delta.days * 30))
    df2 = df.loc[df['Date Complete'] > str(days_before),]
    print('To-Dos completed in last 30 days:',len(df2))
    
def find_to_do_progress(df = None):
    '''
    Show information for all to-do progress
    '''
    # use local DF if calling command with no params
    global lDF
    if df is None:
        df = lDF

    todos_complete = 0
    todos_in_progress = 0
    for i in range(len(df)):
        if df.iloc[i][2] is pd.NaT:
            todos_in_progress +=1
        else:
            todos_complete += 1  
    print('\nTo-Dos Complete:', todos_complete, '\nTo-Dos In Progress:', todos_in_progress)
    return (todos_complete, todos_in_progress)

def find_next_to_dos(df = None):
    '''
    Show next to-dos
    '''
    df = df.loc[df['Date Complete'].isnull(), ['To-Dos', 'Date Assigned', 'Priority']]
    df = df.loc[df['Priority'] > 0, ['To-Dos', 'Date Assigned', 'Priority']]
    df = df.sort_values(by=['Priority', 'Date Assigned'], ascending = False)
    print(df)
    to_do(0, df)

def set_ldf(x):
    global lDF
    lDF = x
    
lDF = None