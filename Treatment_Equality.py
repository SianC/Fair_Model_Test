# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:31:21 2024

@author: sianc
"""

def bin_treat_eq(df, bias_column_name, ground_truth_name, results_common_name):
    
    df_0 = df[df[bias_column_name]==0] # A=0
    df_1 = df[df[bias_column_name]==1] # A=1
    
    df_0_0 = df_0[df_0[ground_truth_name]==0] # A=0, False GT
    df_1_0 = df_1[df_1[ground_truth_name]==0] # A=1, False GT
    FP_0 = sum(list(df_0_0[results_common_name])) # FP - A=0, False GT, Sum of predictions 
    FP_1 = sum(list(df_1_0[results_common_name])) # FP - A=1, False GT, Sum of predictions 
    
    df_0_1 = df_0[df_0[ground_truth_name]==1] # A=0, True GT
    df_1_1 = df_1[df_1[ground_truth_name]==1] # A=0, True GT
    FN_0 = sum(list(df_0_1[results_common_name])) # FN - A=0, True GT, All predictions - sum of predictions
    FN_1 = sum(list(df_1_1[results_common_name])) # FN - A=1, True GT, All predictions - sum of predictions
    
    if FP_0 == 0:
        t1 = 0 
    else:
        t1 = FN_0/FP_0
    
    if FP_1 == 0:
        t2 = 0 
    else:
        t2 = FN_1/FP_1
    te = t1 - t2
    
    return te