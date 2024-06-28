from sklearn.model_selection import train_test_split

def split_data(df, test_sz):
    #df is a dataframe consisting of 4 columns named V1, V2, V3 and V4 where V4 is the outcome and V1-V3 are predictors
    
    predictors = df[["V1", "V2","V3"]]
    predictions = df[["V4"]]
    
    X_train, X_test, y_train, y_test = train_test_split(predictors, predictions, test_size=test_sz, random_state=42)
    
    return X_train, X_test, y_train, y_test

