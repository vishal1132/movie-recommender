#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 00:40:35 2018

@author: vishal
"""

import pandas as pd

df=pd.read_csv("with_url.csv")
df=df.drop("Unnamed: 0",axis=1)
df_all_keywords=df['cast'].astype(str)+df['genres'].astype(str)+df['keywords'].astype(str)+df['production_companies'].astype(str)+df['production_countries'].astype(str)
df_title=df['titles']
df_urls=df['urls']
df_all_keywords=pd.concat([df_all_keywords,df_title,df_urls],axis=1)
df_all_keywords=df_all_keywords.rename(columns={"0":"bag of words"})
df_all_keywords.to_csv("final_processed_with_urls.csv")
#df_urls=df_urls.rename(columns={"0":"urls"})

#df_all_keywords.to_csv('processed_final.csv')
