# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 08:21:20 2023

@author: chama
"""

import pandas as pd

data = [1,2,3,4,5]

s = pd.Series(data)
s

index = ['Linea' + str(i) for i in range(5)]

s = pd.Series(data = data, index = index)
s

data = {'Linea' + str(i) : i+1 for i in range(5)}

s = pd.Series(data)
s

s1 = s + 2

s1

s2 = s1 + s

s,s1,s2


#EJEMPLOS:

datos = {'A': {'X': 1, 'Y': 3}, 'B': {'X': 2, 'Y': 4}}
df = pd.DataFrame(datos)
df

datos = [('A', 'B'), ('C', 'D')]
df = pd.DataFrame(datos, columns = ['L1', 'L2'],  index = ['C1', 'C2'])
df

df1 = pd.DataFrame({'A': {'X': 1}, 'B': {'X': 2}})
df2 = pd.DataFrame({'C': {'X': 3}, 'D': {'X': 4}})
pd.concat([df1, df2])

datos = [[1, 2, 3], [4, 5, 6]]
index = 'X,Y'.split(',')
columns = list('CBA')[::-1]
df = pd.DataFrame(datos, index, columns)
df
