# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:46:16 2019

@author: BeauChapman
"""

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
df=pd.read_csv(r'C:\Users\BeauChapman\bbcpython\Scripting Project.csv', header=None)

#counts number of values for each column.
df.count()

list_of_column_names=['ID',
                      'Name',
                      'Age',
                      'Team',
                      'League',
                      'Games',
                      'PlateAppearances',
                      'AtBats',
                      'Runs',
                      'hits',
                      '2B',
                      '3B',
                      'HomeRuns',
                      'RBI',
                      'StolenBases',
                      'CS',
                      'BB',
                      'SO',
                      'BA',
                      'OBP',
                      'SLG',
                      'OPS',
                      'OPS+',
                     'TB',
                     'GDP',
                     'HBP',
                     'SH',
                     'SF',
                     'IBB',
                     'POS Summary']

dict_of_column_names= { i : list_of_column_names[i] for i in range(0, len(list_of_column_names) ) }


df=df.rename(columns=dict_of_column_names)

#counts null/NAN values per columns
df.isna().sum()

#drop all null values
df=df.dropna()

#confirm no null values in any column of dataframe
df.isna().sum()

#basic statistics info for plateappearances column.  can substitutde plate appearances with any column
df[['PlateAppearances']].describe()

#groupby Team column and show mean for each remaining column, sorted by RBI descending.  round() function specifies number of decimal points
report1 = df.groupby('Team').mean().sort_values('RBI',ascending=False).round(2)

#selects rows where player has RBI greater than 100.  Similar to SELECT * WHERE Col_name > value_in_col
#report2 = df.loc[df['RBI'] > 100]
#creates a report which puts report 1 on sheet 1 of an excel workbook and report 2 on sheet 2
#writer = pd.ExcelWriter('report.xlsx')
#report1.to_excel(writer, 'Sheet1')
#report2.to_excel(writer, 'Sheet2')
#writer.save()

report1

df['TB/PA'] = df['TB']/df['PlateAppearances']
# Get names of indexes for which column PlateAppearances has value < 500
indexNames = df[ df['PlateAppearances'] < 500 ].index
# Delete these row indexes from dataFrame
df.drop(indexNames , inplace=True)

#df.PlateAppearances > 300

df

df.sort_values('TB/PA', ascending=False)

df2 = df.drop(['Age', 'Team', 'League', 'Games', 'AtBats', 'Runs', 'RBI', 'StolenBases', 'CS', 'BA', 'OBP', 'SLG', 'OPS', 'OPS+', 'IBB','POS Summary', 'ID'], axis=1)

df2

import matplotlib.pyplot as plt

hist = plt.xlabel ('TB/PA')
hist = plt.ylabel ('Frequency')
hist = plt.hist(df['TB/PA'])




plt.xlabel ('ID')
plt.ylabel ('TB/PA')
plt.title('Scatterplot of TB/PA')
plt.ylim(.3, .6)
plt.scatter(df['ID'], df['TB/PA'])

#import statsmodels.api as sm

import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats

x = df2.drop(['TB/PA', 'Name'], axis=1)
x = x.apply(pd.to_numeric, errors='coerce')
x.isna().sum()
y = df['TB/PA']
y = y.apply(pd.to_numeric, errors='coerce')

x2 = sm.add_constant(x)
est =sm.OLS(y, x2)
est2 = est.fit()
print(est2.summary())




