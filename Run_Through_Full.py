import numpy as np
import pandas as pd
from os import listdir
from os.path import join, isfile
import Conf_Mat
import LR_model
import DT_model
import RF_model
import SVM_model
import KNN_model
import Split_data
import Results_df_create
from time import time
#Import
import Statistical_Parity as SP
import Equalised_Odds as EO
import Treatment_Equality as te
import CtF_DE as CtF
from sklearn.metrics import balanced_accuracy_score, precision_score, recall_score, roc_auc_score, f1_score

i=0
path = r"Path"
for filename in listdir(path):
    full_path = join(path, filename)
    if isfile(full_path):
        data = pd.read_csv(full_path)
        df = data.drop(data.columns[0], axis=1)
        
        ## Split data
        X_train, X_test, y_train, y_test = Split_data.split_data(df, 0.4)

        ## Create results df
        results_df = Results_df_create.create_results_df(X_test, y_test)
        
        #Logistic Regression - test model
        LR_Results = LR_model.train_LR_model(X_train, y_train).predict(X_test)
        #Logistic Regression - Save results
        results_df["LR"] = LR_Results
        #Logistic Regression - Confusion Matrix
        Conf_Mat.Create_Conf_Mat("Logistic Regression_", filename, y_test, LR_Results, [0,1])
        
        
        #Decision Tree - test model
        DT_Results = DT_model.train_DT_model(X_train, y_train).predict(X_test)
        #Decision Tree - Save results
        results_df["DT"] = DT_Results
        #Decision Tree - Confusion Matrix
        Conf_Mat.Create_Conf_Mat("Decision Tree_", filename, y_test, DT_Results, [0,1])
        
        #Record current time
        start = time()
        #Random Forest - test model
        RF_Results = RF_model.train_RF_model(X_train, y_train).predict(X_test)
        #Random Forest - save results
        results_df["RF"] = RF_Results
        #Random_Forest - Confusion Matrix
        Conf_Mat.Create_Conf_Mat("Random_Forest_", filename, y_test, RF_Results, [0,1])
        #Record current time
        end = time()
        #Report execution time
        result = end - start
        print('%.3f seconds' % result)
        
        #Record current time
        start = time()
        #SVM - test model
        SVM_Results = SVM_model.train_SVM_model(X_train, y_train).predict(X_test)
        #SVM - save results
        results_df["SVM"] = SVM_Results
        #SVM - Confusion Matrix
        Conf_Mat.Create_Conf_Mat("SVM_", filename, y_test, SVM_Results, [0,1])
        #Record current time
        end = time()
        #Report execution time
        result = end - start
        print('%.3f seconds' % result)
        
        #KNN - test model
        KNN_Results = KNN_model.train_KNN_model(X_train, y_train).predict(X_test)
        #KNN - save results
        results_df["KNN"] = KNN_Results
        #KNN - Confusion Matrix
        Conf_Mat.Create_Conf_Mat("KNN_", filename, y_test, KNN_Results, [0,1])
        
        results_df.to_csv("Path_"+filename, index=False)

    
        



