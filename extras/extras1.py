# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:56:45 2023

@author: chama
"""

import pandas as pd

json = open('alquiler.json')
print(json.read())

df_json = pd.read_json('alquiler.json')
df_json

txt = open('alquiler.txt')
print(txt.read())

df_txt = pd.read_table('alquiler.txt')
df_txt

df_xlsx = pd.read_excel('alquiler.xlsx')
df_xlsx

df_html = pd.read_html('datos_html_1.html')
