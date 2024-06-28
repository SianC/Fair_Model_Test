from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV

def train_KNN_model(X_train, y_train):
    #X_train is a dataframe, y_train is a dataframe with 1 column
    
    #Parameters for the grid search
    params = [{'knn__n_neighbors': [3, 5, 7, 9],
             'knn__weights': ['uniform', 'distance'],
             'knn__leaf_size': [10, 15, 20]}]
    
    #Create the model
    knn_pipe = Pipeline([('mms', MinMaxScaler()),
                         ('knn', KNeighborsClassifier())])
    
    #Add the parameters to the model
    gs_knn = GridSearchCV(knn_pipe,
                          param_grid=params,
                          scoring='accuracy',
                          cv=5)
    
    #Train the model
    gs_knn.fit(X_train, y_train.values.ravel())
    
    return gs_knn
