# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:27:33 2023

@author: chama
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.rc('figure', figsize = (14,6))

datos = pd.read_csv('alquiler_residencial.csv', sep = ';')
datos.head(10)

datos.boxplot(['Valor'])

datos[datos['Valor'] >= 500000]

valor = datos['Valor']

Q1 = valor.quantile(.25)
Q3 = valor.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ

seleccion = ((valor >= limite_inferior) & (valor <= limite_superior))

datos_new = datos[seleccion]

datos_new.boxplot(['Valor'])

datos.hist(['Valor'])#No se peude tomar una decision en base a esto

datos_new.hist(['Valor'])#Comparacion de cuando teniamos los outliers a cuando no

datos.boxplot(['Valor'], by = ['Tipo'])


grupo_tipo = datos.groupby('Tipo')['Valor']#Guarda 1 sola columna
type(grupo_tipo)

grupo_tipo.groups

Q1 = grupo_tipo.quantile(.25)
Q3 = grupo_tipo.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ

limite_inferior

datos_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    eh_tipo = datos['Tipo'] == tipo
    eh_dentro_limite = (datos['Valor']>= limite_inferior[tipo]) & (datos['Valor'] <= limite_superior[tipo])
    seleccion = eh_tipo & eh_dentro_limite
    datos_seleccion = datos[seleccion]
    datos_new = pd.concat([datos_new, datos_seleccion])
    
datos_new.boxplot(['Valor'], by = ['Tipo'])

datos_new.to_csv('alquiler_residencial_final.csv', sep = ';', index = False)
