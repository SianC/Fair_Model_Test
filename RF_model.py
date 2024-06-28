from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier


def train_RF_model(X_train, y_train):
    #X_train is a dataframe, y_train is a dataframe with 1 column
    
    #parameters for the grid search
    param_grid = {
        'bootstrap': [True],
        'max_depth': [50, 60, 70, 80],
        'max_features': [2, 3],
        'min_samples_leaf': [1, 2, 3, 4],
        'min_samples_split': [2, 4, 6, 8],           
        'n_estimators': [80, 100, 120]
    }
    
    
    #Set up the model
    clf_RF = RandomForestClassifier(random_state=0, n_jobs=4)
    
    #Add the parameters to the model
    clf_RF = GridSearchCV(estimator = clf_RF, param_grid = param_grid, 
                              cv = 3, n_jobs = -1, verbose = 2)
    
    #Train the model
    clf_RF.fit(X_train, y_train.values.ravel())
    
    return clf_RF

