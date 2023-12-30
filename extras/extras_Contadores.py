# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:55:28 2023

@author: chama
"""

import pandas as pd

s = pd.Series(list('asdaesdaesdasesda'))
s

s.unique()

s.value_counts()

datos = pd.read_csv('../data/alquiler.csv', sep = ';')
datos.head(10)

datos.Tipo.unique()

datos.Tipo.value_counts()

##EJERCICIOS

m1 = 'CCcCCccCCCccCcCccCcCcCCCcCCcccCCcCcCcCcccCCcCcccCc'
m2 = 'CCCCCccCccCcCCCCccCccccCccCccCCcCccCcCcCCcCccCccCc'
m3 = 'CccCCccCcCCCCCCCCCCcccCccCCCCCCccCCCcccCCCcCCcccCC'
m4 = 'cCCccCCccCCccCCccccCcCcCcCcCcCcCCCCccccCCCcCCcCCCC'
m5 = 'CCCcCcCcCcCCCcCCcCcCCccCcCCcccCccCCcCcCcCcCcccccCc'

eventos = {'m1': list(m1), 
                'm2': list(m2), 
                'm3': list(m3), 
                'm4': list(m4), 
                'm5': list(m5)}
monedas = pd.DataFrame(eventos)
df = pd.DataFrame(data = ['Cara', 'Crown'], 
                    index = ['c', 'C'], 
                    columns = ['Faces'])
for item in monedas:
    df = pd.concat([df, monedas[item].value_counts()], 
                    axis = 1)
df