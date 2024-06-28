from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

def train_LR_model(X_train, y_train):
    #X_train is a dataframe, y_train is a dataframe with 1 column
    
    #Parameters for the grid search
    parameters = [{'solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']},
                   {'penalty':['none', 'elasticnet', 'l1', 'l2']},
                   {'C':[0.001, 0.01, 0.1, 1, 10, 100]}]
    
    #Create model
    clf_LR = LogisticRegression(random_state=0)
    
    #Set parameters to model
    clf_LR  = GridSearchCV(estimator = clf_LR,  
                               param_grid = parameters,
                               scoring = 'accuracy',
                               cv = 5,
                               verbose=0)
    
    #Train model
    clf_LR.fit(X_train, y_train.values.ravel())
    
    return clf_LR

