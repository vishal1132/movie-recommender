#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:36:47 2018

@author: vishal
"""

import pandas as pd
import ast

#only the useful columns are selected after writing the useful columns to
# a csv file
df=pd.read_csv("useful_without_chinese.csv")
df=df.drop(['Unnamed: 0'],axis=1)

#editing production countries column and extracting the useful information only
df_production_countries=df['production_countries']


#converting series object to dataframe pandas
df_production_countries=df_production_countries.to_frame()

#iterating over dataframe
for index,rows in df_production_countries.iterrows():
#
    content=""
#iterating over every row using index    
    item=df_production_countries.iloc[index]['production_countries']
    item=ast.literal_eval(item)
    for i in range(len(item)):
        content+=""+str(item[i]['name'])+","
    content=content[:-1]
    content=content.replace(" ","")
    content=content.replace(","," ")
    df_production_countries.iloc[index]['production_countries']=content
df_production_countries.to_csv('production_countries.csv')
