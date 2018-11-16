#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:00:34 2018

@author: vishal
"""

import pandas as pd

df=pd.read_csv("title.csv")
df=df.shift(1)
df=df.rename(columns={'Avatar':'titles'})
df.at[0,'titles']="Avatar"
df.at[4724,'titles']="My Date with Andrew"

for index,rows in df.iterrows():
    df.at[index,'titles']=df.at[index,'titles'].lower()
df.to_csv('lowercase_titles.csv')