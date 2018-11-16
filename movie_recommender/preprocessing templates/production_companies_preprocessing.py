#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:33:43 2018

@author: vishal
"""


import pandas as pd
import ast

#only the useful columns are selected after writing the useful columns to
# a csv file
df=pd.read_csv("useful_without_chinese.csv")
df=df.drop(['Unnamed: 0'],axis=1)

#editing genre column and extracting the useful information only
df_production_companies=df['production_companies']

#converting series object to dataframe pandas
df_production_companies=df_production_companies.to_frame()

for index,rows in df_production_companies.iterrows():
    content=""
    item=df_production_companies.iloc[index]['production_companies']
    item=ast.literal_eval(item)
    for i in range(len(item)):
        content+=""+str(item[i]['name'])+","
    content=content[:-1]
    content=content.replace(" ","")
    content=content.replace(","," ")
    df_production_companies.iloc[index]['production_companies']=content    
df_production_companies.to_csv('production_companies.csv')  