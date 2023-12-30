# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:27:31 2023

@author: chama
"""

import pandas as pd

datos = pd.read_csv('alquiler_residencial.csv', sep = ';')


datos.head(10)

datos.isnull()

datos.notnull()

datos.info()

datos[datos['Valor'].isnull()]

A = datos.shape[0]

datos.dropna(subset = ['Valor'], inplace = True)

B = datos.shape[0]

diferencia = A-B
diferencia

#Ya no hay valores nulos
datos[datos['Valor'].isnull()]

#Mantenimiento e impuestos tambien tienen valores nulos, que haremos con ellos?

#Eliminar los nulos de mantenimiento solo si son departamentos

datos['Mantenimiento'].isnull()

datos[datos['Mantenimiento'].isnull()].shape[0]

seleccion = (datos['Mantenimiento'].isnull()) & (datos['Tipo'] == 'Departamento')

A = datos.shape[0]

datos = datos[~seleccion]

B = datos.shape[0]

diferencia = A-B
diferencia
#Se eliminaron 745 lineas

datos[datos['Mantenimiento'].isnull()].shape[0]
#Aun quedan valores nulos, pero podemos reemplazarlos por valores nulos

datos = datos.fillna({'Mantenimiento':0, 'Impuesto':0})

datos

datos[datos['Mantenimiento'].isnull()].shape[0]
datos[datos['Impuesto'].isnull()].shape[0]
#Ya no hay nulos

datos


#Exportar archivo

datos.to_csv('alquiler_residencial.csv', sep = ';', index = False)


#EJERCICIOS

inmuebles= pd.DataFrame([['Departamento', None, 970, 68], 
                        ['Departamento', 2000, 878, 112], 
                        ['Casa', 5000, None, 500], 
                        ['Departamento', None, 1010, 170], 
                        ['Departamento', 1500, 850, None], 
                        ['Casa', None, None, None], 
                        ['Departamento', 2000, 878, None], 
                        ['Departamento', 1550, None, 228], 
                        ['Departamento', 2500, 880, 195]], 
                        columns = ['Tipo', 'Valor', 'Mantenimiento', 'Impuesto'])
inmuebles.dropna(subset = ['Valor'], inplace = True)

