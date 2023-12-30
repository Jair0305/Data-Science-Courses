# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:48:21 2023

@author: chama
"""

import pandas as pd

datos = pd.read_csv('alquiler_residencial.csv', sep = ';')

datos.head(10)

datos['Valor Bruto'] = (datos['Valor']) + (datos['Mantenimiento']) + (datos['Impuesto'])

datos.head(10)

datos['Valor m2'] = (datos['Valor'])/(datos['Area'])
datos.head(10)

datos['Valor m2'] =datos['Valor m2'].round(2)
datos.head(10)

datos['Valor Bruto m2'] = ((datos['Valor Bruto'])/(datos['Area'])).round(2)
datos.head(10)

datos


casa = ['Casa', 'Casa en condominio', 'Casa de villa']

datos['Tipo agrupado'] = datos['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Departamento')
datos

#EJERCICIOS

import pandas as pd
alumnos = pd.DataFrame({
'Nombre': ['Ary', 'Katia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
'Edad': [15, 27, 56, 32, 42, 21, 19, 35], 
'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6]}, 
columns = ['Nombre', 'Edad', 'Sexo', 'Notas'])


#Borrar datos

datos_aux = pd.DataFrame(datos[['Tipo agrupado', 'Valor m2', 'Valor Bruto', 'Valor Bruto m2']])

datos_aux

del datos_aux['Valor Bruto']
datos_aux

datos_aux.pop('Valor Bruto m2')#Muestra en la consola lo que acabas de borrar
datos_aux

datos.head(10)
datos.drop(['Valor Bruto', 'Valor Bruto m2'],  axis = 1, inplace = True)#axis = 1 es para borrar columnas, ayq ue si no lo suamos, bsucara para borrar filas
datos.head(10)

datos.to_csv('alquiler_residencial.csv', sep = ';', index = False)

