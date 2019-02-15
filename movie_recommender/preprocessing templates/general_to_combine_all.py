#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 21:00:13 2018

@author: vishal
"""
import pandas as pd

df_cast=pd.read_csv("cast.csv")
df_cast=df_cast.drop('Unnamed: 0',axis=1)
df_genre=pd.read_csv("genres.csv")
df_genre=df_genre.drop('Unnamed: 0',axis=1)
df_keywords=pd.read_csv("keywords.csv")
df_keywords=df_keywords.drop('Unnamed: 0',axis=1)
df_production_companies=pd.read_csv("production_companies.csv")
df_production_companies=df_production_companies.drop('Unnamed: 0',axis=1)
df_production_countries=pd.read_csv("production_countries.csv")
df_production_countries=df_production_countries.drop('Unnamed: 0',axis=1)
df_title=pd.read_csv("title.csv")
df_title=df_title.shift(1)
df_title.iloc[[0]]="Avatar"
df_title=df_title.drop('0',axis=1)
df_title=df_title.rename(columns={'Avatar':'title'})
df_useful=pd.concat([df_cast,df_genre,df_keywords,df_production_companies,df_production_countries,df_title],axis=1)
#df_useful.to_csv("processed_dataset.csv")