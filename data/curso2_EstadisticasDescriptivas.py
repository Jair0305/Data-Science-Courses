# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:18:00 2023

@author: chama
"""

import pandas as pd

datos = pd.read_csv('alquiler_residencial.csv', sep = ';')

datos.head(10)

#datos['Valor'].mean()
#barrios = ['Ate','Barranco','Comas','Lince','El Agustino','San Luis','Callao']
#seleccion = datos['Distrito'].isin(barrios)
#datos = datos[seleccion]

datos.head(10)

datos['Distrito'].drop_duplicates()

grupo_barrio = datos.groupby('Distrito')

type(grupo_barrio)

grupo_barrio.groups

for barrio, data in grupo_barrio:
    print('{} -> {}'.format(barrio, data.Valor.mean()))
    

grupo_barrio[['Valor', 'Mantenimiento']].mean().round(2)


grupo_barrio['Valor'].describe().round(2)

grupo_barrio['Valor'].aggregate(['min','max']).rename(columns = {'min': 'Minimo', 'max': 'Maximo'})


import matplotlib.pyplot as plt
plt.rc('figure', figsize = (20,10))

fig = grupo_barrio['Valor'].mean().plot.bar(color = 'blue')
fig.set_ylabel('Valor del Alquiler')
fig.set_title('Valor medio del alquiler por distrito', {'fontsize': 22})


fig = grupo_barrio['Valor'].max().plot.bar(color = 'blue')
fig.set_ylabel('Valor del Alquiler')
fig.set_title('Valor Maximo del alquiler por distrito', {'fontsize': 22})

