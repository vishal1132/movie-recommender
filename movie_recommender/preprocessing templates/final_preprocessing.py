#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 21:18:27 2018

@author: vishal
"""

import pandas as pd

df=pd.read_csv("processed_dataset.csv")
df=df.drop('Unnamed: 0',axis=1)
df_all_keywords=df['cast'].astype(str)+df['genres'].astype(str)+df['keywords'].astype(str)+df['production_companies'].astype(str)+df['production_countries'].astype(str)
df_title=df['title']
df_all_keywords=pd.concat([df_all_keywords,df_title],axis=1)
df_all_keywords.to_csv('processed_final.csv')