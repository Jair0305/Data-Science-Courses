# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 16:52:05 2023

@author: chama
"""

import pandas as pd

datos = pd.read_csv('alquiler_residencial.csv', sep = ";")

datos.head(10)


#Seleccione los inmuebles clasificados por Departamento


seleccion = datos['Tipo'] == 'Departamento'
seleccion

n1 = datos[seleccion].shape[0]
n1


seleccion = (datos['Tipo'] == 'Casa') | (datos['Tipo'] == 'Casa en condominio') | (datos['Tipo'] == 'Casa de villa')

n2 = datos[seleccion].shape[0]
n2

seleccion = (datos['Area'] >=60) & (datos['Area'] <= 100)

n3 = datos[seleccion].shape[0]
n3

seleccion  = (datos['Cuartos'] >= 4) & (datos['Valor'] < 2000)
n4 = datos[seleccion].shape[0]
n4


#EJERCICIOS

import pandas as pd
alumnos = pd.DataFrame({
'Nombre': ['Ary', 'Katia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
'Edad': [15, 27, 56, 32, 42, 21, 19, 35], 
'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6], 
'Aprobado': [True, False, False, True, True, True, False, False]},
columns = ['Nombre', 'Edad', 'Sexo', 'Notas', 'Aprobado'])
