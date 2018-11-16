#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:18:34 2018

@author: vishal
"""

import pandas as pd
import ast

#only the useful columns are selected after writing the useful columns to
# a csv file
df=pd.read_csv("useful_without_chinese.csv")
df=df.drop(['Unnamed: 0'],axis=1)

#editing genre column and extracting the useful information only
df_cast=df['cast']

#converting series object to dataframe pandas
df_cast=df_cast.to_frame()

for index,rows in df_cast.iterrows():
    content=""
    item=df_cast.iloc[index]['cast']
    item=ast.literal_eval(item)
    for i in range(len(item)):
        content+=""+str(item[i]['name'])+","
    content=content[:-1]
    content=content.replace(" ","")
    content=content.replace(","," ")
    content=content.split()
    if len(content)==0:
        first=""
        second=""
        third=""
        fourth=""
    else:        
        if len(content)==1:
            first=content[0]
            second=""
            third=""
            fourth=""
        else:
            if len(content)==2:
                first=content[0]
                second=content[1]
                third=""
                fourth=""
            else:
                if len(content)==3:
                    first=content[0]
                    second=content[1]
                    third=content[2]
                    fourth=""
                else:
                    first=content[0]
                    second=content[1]
                    third=content[2]
                    fourth=content[3]
    content=""+first+" "+second+" "+third+" "+fourth
    df_cast.iloc[index]['cast']=content    
df_cast.to_csv('cast.csv')