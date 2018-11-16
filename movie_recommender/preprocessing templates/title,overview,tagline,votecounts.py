#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:54:53 2018

@author: vishal
"""

import pandas as pd

#only the useful columns are selected after writing the useful columns to
# a csv file
df=pd.read_csv("useful_without_chinese.csv")
df=df.drop(['Unnamed: 0'],axis=1)

df_title=df['original_title']
df_votecounts=df['vote_count']
df_overview=df['overview']
df_overview.to_csv('overview.csv')
df_votecounts.to_csv('votecount.csv')
df_title.to_csv('title.csv')