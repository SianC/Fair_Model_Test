# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:23:19 2024

@author: sianc
"""

def bin_eq_odds(df, bias_column_name, ground_truth_name, results_common_name):
    
    df_0 = df[df[bias_column_name]==0]
    df_1 = df[df[bias_column_name]==1]
    
    df_0_0 = df_0[df_0[ground_truth_name]==0]
    df_1_0 = df_1[df_1[ground_truth_name]==0]
    if len(df_0_0) == 0:
        t1 = 0 
    else:
        t1 = sum(df_0_0[results_common_name])/len(df_0_0)
    if len(df_1_0) == 0:
        t2 = 0 
    else:
        t2 = sum(df_1_0[results_common_name])/len(df_1_0)
    df_a_0 = t1 - t2
    
    df_0_1 = df_0[df_0[ground_truth_name]==1]
    df_1_1 = df_1[df_1[ground_truth_name]==1]
    if len(df_0_1) == 0:
        t3 = 0 
    else:
        t3 = sum(df_0_1[results_common_name])/len(df_0_1)
    if len(df_1_1) == 0:
        t4 = 0 
    else:
        t4 = sum(df_1_1[results_common_name])/len(df_1_1)
    df_a_1 = t3 - t4
    
    return [df_a_0, df_a_1]
    