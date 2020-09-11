# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:03:39 2020

@author: jialing
"""
import pandas as pd
import numpy as np

last_year_file='科系D-108指考.csv'
conversion_table_file='OutputMin.csv'

last_year = pd.read_csv(last_year_file,encoding='ANSI')
conversion_table = pd.read_csv(conversion_table_file,encoding='utf-8')
aa=last_year.merge(conversion_table,how = 'left',on=['UName','DName'])

aa.to_csv('OutputLastMin.csv',encoding='utf-8-sig',index=False)
