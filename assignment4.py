# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:52:03 2020

@author: vmunavalli
"""

# It happens all the time: someone gives you data containing malformed strings,
# Python, lists and missing data. How do you tidy it up so you can get on with the
# analysis?
# Take this monstrosity as the DataFrame to use in the following puzzles:
# df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
# 'londON_StockhOlm',
# 'Budapest_PaRis', 'Brussels_londOn'],
# 'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
# 'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
# 'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
# '12. Air France', '"Swiss Air"']})
# 1. Some values in the the FlightNumber column are missing. These numbers are
# meant to increase by 10 with each row so 10055 and 10075 need to be put in
# place. Fill in these missing numbers and make the column an integer column
# (instead of a float column).

import pandas as pd
import numpy as np
import matplotlib as plot

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

for i in range(1, len(df)):    
        df.loc[i, 'FlightNumber'] = df.loc[i-1, 'FlightNumber'] +10


# 2. The From_To column would be better as two separate columns! Split each
# string on the underscore delimiter _ to give a new temporary DataFrame with
# the correct values. Assign the correct column names to this temporary
# DataFrame.

for i in range(0, len(df)):    
        df.loc[i, 'From_To_Removed_Delimetter'] = df.loc[i, 'From_To'].replace('_',' ').capitalize()
#print(df)

# . Notice how the capitalisation of the city names is all mixed up in this
# temporary DataFrame. Standardise the strings so that only the first letter is
# uppercase (e.g. "londON" should become "London".)
for i in range(0, len(df)):    
        df.loc[i, 'From_To'] = df.loc[i, 'From_To'].capitalize()
#print(df)


# Delete the From_To column from df and attach the temporary DataFrame
# from the previous questions
del df['From_To']
#print(df)


# 5. In the RecentDelays column, the values have been entered into the
# DataFrame as a list. We would like each first value in its own column, each 
# second value in its own column, and so on. If there isn't an Nth value, the value
# should be NaN.
# Expand the Series of lists into a DataFrame named delays, rename the columns
# delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df
# with delays.

for i in range(0, len(df['RecentDelays'])):  
    df['delay_',i] =pd.Series(df.loc[i, 'RecentDelays'])  
print(df)
