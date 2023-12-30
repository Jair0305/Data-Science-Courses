# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 16:21:27 2023

@author: chama
"""

import pandas as pd

datos = pd.read_csv('alquiler.csv', sep = ';')

datos.head(10)

residencial = ['Habitación',
 'Casa',
 'Departamento',
 'Casa en condominio',
 'Casa comercial',
 'Casa de villa']

residencial

datos.head(10)

seleccion = datos['Tipo'].isin(residencial)

datos_residencial = datos[seleccion]

datos_residencial

list(datos_residencial['Tipo'].drop_duplicates())

datos_residencial.shape[0]

datos.shape[0]

datos_residencial.index = range(datos_residencial.shape[0])

datos_residencial

#EXPORTAR BASE DE DATOS

datos_residencial.to_csv('alquiler_residencial.csv', sep = ';')

datos_residencial2 = pd.read_csv('alquiler_residencial.csv', sep = ';')

datos_residencial2

datos_residencial.to_csv('alquiler_residencial.csv', sep = ';', index = False)

datos_residencial2 = pd.read_csv('alquiler_residencial.csv', sep = ';')

datos_residencial2

datos_residencial2.columns.name = 'Index'

datos_residencial2
