# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:42:51 2024

@author: sianc
"""

#Import
import numpy as np
import pandas as pd
import Statistical_Parity as SP
import Equalised_Odds as EO
import Treatment_Equality as te
import CtF_DE as CtF
from os import listdir
from os.path import join, isfile

path = r"Path"
#SP_Ground, EO_Ground, TE_Ground, DE_Ground, IE_Ground, SE_Ground = [], [], [], [], [], []
#SP_LRr, EO_LRr, TE_LRr, DE_LRr, IE_LRr, SE_LRr = [], [], [], [], [], []
#SP_DTr, EO_DTr, TE_DTr, DE_DTr, IE_DTr, SE_DTr = [], [], [], [], [], []
#SP_RFr, EO_RFr, TE_RFr, DE_RFr, IE_RFr, SE_RFr = [], [], [], [], [], []
#SP_SVMr, EO_SVMr, TE_SVMr, DE_SVMr, IE_SVMr, SE_SVMr = [], [], [], [], [], []
#SP_KNNr, EO_KNNr, TE_KNNr, DE_KNNr, IE_KNNr, SE_KNNr = [], [], [], [], [], []
SP_list, EO_list, TE_list, DE_list, IE_list, SE_list = [], [], [], [], [], []
Ground_Truth = "Ground_Truth"
items = [Ground_Truth, "LR", "DT", "RF", "SVM", "KNN"]

for filename in listdir(path):
    full_path = join(path, filename)
    if isfile(full_path):
        print(filename)
        df = pd.read_csv(full_path)
        results_df = pd.DataFrame()
        SP_list, EO_list, TE_list, DE_list, IE_list, SE_list = [], [], [], [], [], []
        for name in items:
            SP_list.append(SP.bin_stat_par(df, "V2", name))
            #DE_list.append(CtF.DE(df, "V1", name, "V2", "V3"))
            #IE_list.append(CtF.IE(df, "V1", name, "V2", "V3"))
            #SE_list.append(CtF.SE(df, "V1", name, "V2", "V3"))
            if name == Ground_Truth:
                EO_list.append(0)
                TE_list.append(0)
            else:
                EO_list.append(EO.bin_eq_odds(df, "V2", Ground_Truth, name))
                TE_list.append(te.bin_treat_eq(df, "V2", Ground_Truth, name))
        print("Saving results")
        results_df["Model"] = items
        results_df["SP_Score"] = SP_list
        results_df["EO_Score"] = EO_list
        results_df["TE_Score"] = TE_list
        #results_df["DE_Score"] = DE_list
        #results_df["IE_Score"] = IE_list
        #results_df["SE_Score"] = SE_list
        results_df.to_csv("Path_"+filename, index=False)
        print(filename)
        
        
        
        
        
        