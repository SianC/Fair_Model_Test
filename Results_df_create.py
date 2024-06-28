import pandas as pd

def create_results_df(X_test, y_test):
    #X_test is a dataframe containing V1, V2 and V3 columns. y_test is a dataframe of a single column
    
    results_df = pd.DataFrame()
    results_df["V1"] = X_test["V1"]
    results_df["V2"] = X_test["V2"]
    results_df["V3"] = X_test["V3"]
    results_df["Ground_Truth"] = y_test
    
    return results_df

