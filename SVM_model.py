from sklearn.model_selection import GridSearchCV
from sklearn import svm


def train_SVM_model(X_train, y_train):
    #X_train is a dataframe, y_train is a dataframe with 1 column
    
    #Parameters for the grid search
    parameters = {
        'max_iter':[900,1000], 
        'C':[1, 10]}
    
    #Create the model
    svc = svm.LinearSVC()
    
    #Add the parameters to the model
    clf_SVM = GridSearchCV(svc, parameters, n_jobs=-1)
    
    #Train the model
    clf_SVM.fit(X_train, y_train.values.ravel())
    
    return clf_SVM
    