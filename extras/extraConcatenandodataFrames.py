# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 08:34:29 2023

@author: chama
"""

import pandas as pd

data = [[1,2,3,],[4,5,6],[7,8,9]]
data

df1 = pd.DataFrame(data = data)
df1

index = ['Linea' + str(i) for i in range(3)]
index

df1 = pd.DataFrame(data = data, index = index)
df1

columns = ['Columna' + str(i) for i in range(3)]
columns

df1 = pd.DataFrame(data = data, index = index, columns = columns)
df1

data = {'Columna0': {'Linea0':1, 'Linea1':4, 'Linea2':7}, 'Columna1': {'Linea0':2, 'Linea1':5, 'Linea2':8}, 'Columna2': {'Linea0':3, 'Linea1':6, 'Linea2':9}}
df2 = pd.DataFrame(data)
df2

data = [(1,2,3), (4,5,6), (7,8,9)]
data

df3 = pd.DataFrame(data, index = index, columns = columns)
df3

df1[df1 > 0] = 'A'
df1

df2[df2 > 0] = 'B'
df2

df3[df3 > 0] = 'C'
df3

df4 = pd.concat([df1,df2,df3])
df4

df5 = pd.concat([df1,df2,df3], axis = 1)
df5