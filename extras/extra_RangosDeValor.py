# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:18:10 2023

@author: chama
"""

import pandas as pd

datos = pd.read_csv('../data/alquiler.csv', sep = ';')
datos.head(10)

#agrupamiento entre 1 y 2 cuartos
#agrupamiento entre 3 y 4 cuartos
#agrupamiento entre 5 y 6 cuartos
#agrupamiento entre 7+ cuartos

clases = [0, 2, 4, 6, 100]

cuartos = pd.cut(datos.Cuartos, clases)
cuartos

pd.value_counts(cuartos)

label = ['1 y 2 cuartos', '3 y 4 cuartos', '5 y 6 cuartos', '7 o mas cuartos']

cuartos = pd.cut(datos.Cuartos, clases, labels = label)
cuartos

pd.value_counts(cuartos)

cuartos = pd.cut(datos.Cuartos, clases, labels = label, include_lowest= True)
pd.value_counts(cuartos)
