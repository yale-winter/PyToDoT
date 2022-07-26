# -*- coding: utf-8 -*-
"""
@author: yale-winter
"""
from datetime import date, timedelta
import pandas as pd
def to_do(i, j=None):
    '''
    Print the to-do description from row id
    '''
    # use local DF if calling command with no params
    global lDF
    if j is None:
        j = lDF
    print('\nTop To-Do:')
    print('>>>', j.iloc[i][0])
def find_recent_progress(j, prog):
    '''
    Show information regarding to-do progress in last 30 days
    '''
    days_before = pd.Timestamp((date.today()-timedelta(days=30)))
    df3 = j.iloc[0, 1]
    delta = pd.Timestamp(date.today()) - pd.Timestamp(df3)
    print('Days since tracking:', delta.days)
    print('Average To-Dos completed in 30 days:', int(prog[0] / delta.days * 30))
    listed = j['Date Complete'].values.tolist()
    k = 0
    for i in range(len(listed)):
        if pd.Timestamp(listed[i]) > days_before:
            k += 1
    print('To-Dos completed in last 30 days:', k)
def find_to_do_progress(j=None):
    '''
    Show information for all to-do progress
    '''
    # use local DF if calling command with no params
    global lDF
    if j is None:
        j = lDF
    todos_complete = 0
    todos_in_progress = 0
    for i in range(len(j)):
        if j.iloc[i][2] is pd.NaT:
            todos_in_progress += 1
        else:
            todos_complete += 1
    print('\nTo-Dos Complete:', todos_complete, '\nTo-Dos In Progress:', todos_in_progress)
    return (todos_complete, todos_in_progress)
def find_next_to_dos(j=None):
    '''
    Show next to-dos
    '''
    j = j.loc[j['Date Complete'].isnull(), ['To-Dos', 'Date Assigned', 'Priority']]
    j = j.loc[j['Priority'] > 0, ['To-Dos', 'Date Assigned', 'Priority']]
    j = j.sort_values(by=['Priority', 'Date Assigned'], ascending=False)
    print(j)
    to_do(0, j)
def set_ldf(i):
    '''
    assign ldf
    '''
    global lDF
    lDF = i
lDF = None
