# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 18:25:53 2023

@author: chama
"""

import pandas as pd

datos = pd.read_csv('alquiler.csv', sep = ';')

datos.head(10)

datos['Tipo']
datos.Tipo

tipo_de_inmueble = datos.Tipo

type(tipo_de_inmueble)

tipo_de_inmueble.drop_duplicates(inplace = True)

tipo_de_inmueble = pd.DataFrame(tipo_de_inmueble)
type(tipo_de_inmueble)

tipo_de_inmueble.shape[0]

range(tipo_de_inmueble.shape[0])

for i in range(tipo_de_inmueble.shape[0]):
    print(i)

tipo_de_inmueble.index = range(tipo_de_inmueble.shape[0])

tipo_de_inmueble.columns.name = 'Id'

tipo_de_inmueble
