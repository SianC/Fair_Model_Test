# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:53:32 2024

@author: sianc
"""

def bin_stat_par(df, bias_column_name, results_column_name):
    
    df_0 = df[df[bias_column_name]==0]
    df_1 = df[df[bias_column_name]==1]
    
    if len(df_0) == 0 or len(df_1) == 0:
        sp = 100
    else:
        sp = sum(df_1[results_column_name])/len(df_1) - sum(df_0[results_column_name])/len(df_0)
    
    return sp



        