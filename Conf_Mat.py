from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def Create_Conf_Mat(Name, file, y_test, model_results, classes):
    #Name is the name of the confusion matrix, this should be a string
    #file is for the name of the confusion matrix, this should be a string
    #y_test is a dataframe of 1 column 
    #model_results is an array the same length as y_test
    #classes is an array of the labels for the confusion matrix
    
    #Create confusion matrix
    cm = confusion_matrix(y_test, model_results)
    disp_LR = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classes)
    disp_LR.plot()
    plt.title(Name+file)
    plt.show()
