# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 19:09:13 2023

@author: chama
"""

import pandas as pd
pd.set_option('display.max_rows',15)

dataset = pd.read_csv('alquiler.csv', sep=';')

dataset.describe()

dataset.info()

type(dataset)

dataset.head(10)

dataset.dtypes

tipo_de_datos = pd.DataFrame(dataset.dtypes, columns=['Tipos de datos'])

tipo_de_datos.columns.name = 'Variables'

tipo_de_datos

dataset.shape

dataset.shape[0]

dataset.shape[1]

print('Labase de datos presenta {} registros (inmuebbles) y {} variables'.format(dataset.shape[0], dataset.shape[1]))
