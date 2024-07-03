# Fair_Model_Test
This code is associated with the fair model testing work

## Data creation
Synthteic data creation can be completed using Data_from_DAG.R

## Data cleaning/ required documents
These documents are needed to be downloaded for the later work:
 - Conf_Mat.py
 - Results_df_create.py
 - Split_data.py

## Model creation
The following documents contain the model creation and gridsearches:
 - DT_model.py
 - KNN_model.py
 - LR_model.py
 - RF_model.py
 - SVM_model.py

## Fairness test creation
The following documents contain the fairness notions:
 - Treatment_equality.py
 - Statistical_parity.py
 - Equalised_Odds.py

## Do the work!
Run_through_full requires inputting the folder containing the datasets and allows you to run and save the results of all 5 models. Note - the Random Forest and SVM output times taken as they are computationally expensive when there is a large amount of data.
Run_trhough_FT requires inputting the folder containing all the results and allows you to run and save the 3 datasets.
Graphs.py creates graphs for the results of the fairness tests
