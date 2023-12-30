# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:57:14 2023

@author: chama
"""

import pandas as pd

data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)

s

s.fillna(0)

s.fillna(method = 'ffill')#LLena los valores nulos con el valor anterior de forma ascendente

s.fillna(method = 'bfill')#Leena los valores nulos con el valor anterior de forma descendente

s.fillna(s.mean())#Llena los valores nulos con el promedio de los datos

s1 = s.fillna(method = 'ffill', limit = 1)#Llena solo el primer valor nulo, si es que existen varios nulos en secuencia

s2 = s1.fillna(method = 'bfill', limit = 1)#LLena los valores faltantes
s2
