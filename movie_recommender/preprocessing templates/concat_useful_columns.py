#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 00:13:59 2018

@author: vishal
"""

import pandas as pd

#loading csv files
df_cast=pd.read_csv("cast.csv")
df_genres=pd.read_csv("genres.csv")
df_keywords=pd.read_csv("keywords.csv")
df_titles=pd.read_csv("lowercase_titles.csv")
df_pro_com=pd.read_csv("production_companies.csv")
df_pro_con=pd.read_csv("production_countries.csv")
df_urls=pd.read_csv("src_urls.csv")

#removind unwanted columns
df_cast=df_cast.drop("Unnamed: 0",axis=1)
df_genres=df_genres.drop("Unnamed: 0",axis=1)
df_keywords=df_keywords.drop("Unnamed: 0",axis=1)
df_pro_com=df_pro_com.drop("Unnamed: 0",axis=1)
df_pro_con=df_pro_con.drop("Unnamed: 0",axis=1)
df_urls=df_urls.drop("Unnamed: 0",axis=1)
df_titles=df_titles.drop("Unnamed: 0",axis=1)
df_titles=df_titles.drop("0",axis=1)

#renaming urls column name
df_urls=df_urls.rename(columns={"0":"urls"})

df_common=pd.concat([df_cast,df_genres,df_keywords,df_pro_com,df_pro_con,df_urls,df_titles],axis=1)

count=0

indexes=[]

for index,rows in df_common.iterrows():
    count+=1
    print(count)
    if df_common.iloc[index]['urls'] == "no url for this movie":
        #df_common=df_common.drop(index)
        indexes.append(index)
df_common=df_common.drop(indexes)
df_common.to_csv("with_url.csv")        