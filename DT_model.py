from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

def train_DT_model(X_train, y_train):
    #X_train is a dataframe, y_train is a dataframe with 1 column
    
    #Parameters for the grid search
    tree_para = [{'criterion': ['entropy', 'gini'], 'max_depth': range(1,10)},
          {'min_samples_leaf': range(1,10)}]
    
    #Set up the model
    clf_DT = DecisionTreeClassifier()
    
    #Add the grid search parameters
    clf_DT = GridSearchCV(clf_DT, tree_para, cv=5)
    
    #Train model
    clf_DT = clf_DT.fit(X_train, y_train.values.ravel())
    
    
    return clf_DT

