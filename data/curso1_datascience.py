# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 15:25:41 2023

@author: chama
"""

import pandas as pd

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)

dataset = pd.read_csv('db.csv', sep = ';')

dataset.dtypes
dataset.info()

#Creando tuplas

#- Utilizando un par de paréntesis: ( )
#- Utilizando una coma a la derecha: x,
#- Utilizando un par de paréntesis con objetos separados por comas: ( x, y, z )
#- Utilizando: tuple() o tuple(iterador)

()
1,2,3

nombre = 'Passat'
valor = 153000

(nombre,valor)

nombres_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox','DS5'])
type(nombres_carros)

#SELECCIONES EN TUPLAS

nombre_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5', ('fusca', 'Gol', 'C4'))

nombre_carros[-1]
nombre_carros[-1][1]

#ITERANDO EN TUPLAS

nombres_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')
for item in nombres_carros:
    print(item)

#DESEMPACANDO TUPLAS

carro_1, carro_2, carro_3, carro_4 = nombres_carros

carro_1
carro_2
carro_3
carro_4

_, A, _, B = nombres_carros


A
B


_, C, *_ = nombres_carros
C

#ZIP()

carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
valores = [88078.64, 106161.94, 72832.16, 124549.07]
list(zip(carros,valores))

#for item in zip(carros,valores):
#    print(item)
    
for carro, valor in zip(carros, valores):
    print(carro, valor)

for carro, valor in zip(carros, valores):
    if(valor > 100000):
        print(carro, valor)

#DICCIONARIOS

carros = ['Jetta Variant', 'Passat', 'Crossfox']
valores = [88078.64, 106161.94, 72832.16]

carros.index('Passat')

valores[carros.index('Passat')]

datos = {'Jetta Variant':88078.64, 'Passat':106161.94, 'Crossfox':72832.16}
type(datos)

#DICCIONARIOS CON ZIP

list(zip(carros, valores))
datos = dict(zip(carros,valores))
datos

datos['Passat']

'Passat' in datos

'Fusca' in datos

'Fusca' not in datos

len(datos)

datos['DS5'] = 124549.07
datos


del datos['Passat']
datos

datos.update({'Passat': 106161.94})

datos.update({'Passat': 106161.96, 'Fusca': 150000})
datos

datosCopy = datos.copy()

datosCopy

del datosCopy['Fusca']
datos
datosCopy

datosCopy.pop('Passat')

datosCopy.pop('Passat', "Llave no fue encontrada")

datosCopy.pop('DS5', "Llave no fue encontrada")

datosCopy

datosCopy.clear()

datosCopy

datos = dict(zip(carros,valores))

datos.update({'Fusca':150000, 'DS5':124549.07})

datos.keys()

for key in datos.keys():
  print(key)

datos.values()

for values in datos.values():
    print(values)
    
#DICT.ITEMS

datos.items()

for item in datos.items():
    print(item)

for key, value in datos.items():
    print(key, '->', value)
    
for key, value in datos.items():
    if(value > 100000):
        print(key)
        
datos = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}


valores = []
for valor in datos.values():
  valores.append(valor)
valores

suma = 0
for valor in datos.values():
    suma+= valor
suma

list(datos.values())

sum(datos.values())

help(print)

def media():
  valor = (1+2+3)/3
  print(valor)
  
media()

def media(n1,n2,n3):
  valor = (n1+n2+n3)/3
  print(valor)

media(5,6,7)

def media(lista):
    valor = sum(lista)/len(lista)
    print(valor)

resultado = media([2,3,4,5,7,5,3,2,4,6,8,8,6,4,32,4,6,2])

type(resultado)


def media(lista):
  valor = sum(lista)/len(lista)
  return(valor)

resultado = media([1,2,3,4,5,6,7,8,9])
resultado

def media(lista):
    valor = sum(lista)/len(lista)
    return(valor, len(lista))

media([1,2,3,4,5,6,7,8,9])

resultado, n = media([1,2,3,4,5,6,7,8,9])

resultado
n

#ESTRUCTURA DE DATOS

import pandas as pd

carros = ['Jetta Variant', 'Passat', 'Crossfox']

pd.Series(carros)

datos = [
    {'Nombre': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Año': 2003, 'Kilometraje': 44410.0, 'Cero_km': False, 'Valor': 88078.64},
    {'Nombre': 'Passat', 'Motor': 'Motor Diesel', 'Año': 1991, 'Kilometraje': 5712.0, 'Cero_km': False, 'Valor': 106161.94},
    {'Nombre': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Año': 1990, 'Kilometraje': 37123.0, 'Cero_km': False, 'Valor': 72832.16}
]

dataset = pd.DataFrame(datos)
dataset

dataset[['Nombre','Año','Kilometraje','Motor']]


datos = {
    'Nombre': ['Jetta Variant', 'Passat', 'Crossfox'],
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8'],
    'Año': [2003, 1991, 1990],
    'Kilometraje': [44410.0, 5712.0, 37123.0],
    'Cero_km': [False, False, False],
    'Valor': [88078.64, 106161.94, 72832.16]
}

dataset = pd.DataFrame(datos)


dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)
dataset
dataset['Valor']
dataset.head()
type(dataset['Valor'])
dataset[['Valor']]

type(dataset[['Valor']])

dataset[0:3]

dataset.loc['Passat']

dataset.loc[['Passat','DS5']]

dataset.loc[:, ['Motor', 'Valor']]

dataset.head()

dataset.iloc[[1]]

dataset.iloc[1:4]

dataset.iloc[1:4, [0,5,2]]

dataset.iloc[[1,42,22], [0,5,2]]

dataset.iloc[:, [0,5,2]]


dataset.head()

dataset.Motor

dataset.Motor == 'Motor Diesel'

type(dataset.Motor == 'Motor Diesel')

dataset[dataset.Motor == 'Motor Diesel']

dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Cero_km == True)]

dataset.query('Motor == "Motor Diesel" and Cero_km == True')

for item in dataset:
    print(item)

list(dataset.iterrows())

for index, row in dataset.iterrows():
    if(2020 - row.Año !=0):
        dataset.loc[index, 'km_media'] = row.Kilometraje / (2020 - row.Año)
    else:
        dataset.loc[index, 'km_media'] = 0
        
dataset

dataset.head()

dataset.info()

dataset.Kilometraje.isna()

dataset[dataset.Kilometraje.isna()]

dataset.fillna(0)

dataset.fillna(0, inplace = True)

dataset

dataset.query('Cero_km == True')

dataset = pd.read_csv('db.csv', sep = ';')

dataset

dataset.dropna(subset = ['Kilometraje'], inplace = True)

dataset
