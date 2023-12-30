# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:11:42 2023

@author: chama
"""

import pandas as pd

'l1 l2 l3 l4'.split()

data = [(1,2,3,4),
        (5,6,7,8),
        (9,10,11,12),
        (13,14,15,16)]

df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())
df

df['c1']

type(df['c1'])

df[['c3','c1']]

type(df[['c3','c1']])

df

df[1:-1]

df[1:][['c1','c3']]

df.loc['l3']

type(df.loc['l3'])

df.loc[['l3','l2']]

df

df.loc['l1','c2']

df.iloc[0,1]

df.loc[['l3','l1'], ['c4','c1']]

df.iloc[[2,0], [3,0]]
