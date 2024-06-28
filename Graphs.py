import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from os import listdir
from os.path import join, isfile


#Read in data
Ground_Truth_SP, LR_SP, DT_SP, RF_SP, SVM_SP, KNN_SP = [], [], [], [], [], []
Ground_Truth_TE, LR_TE, DT_TE, RF_TE, SVM_TE, KNN_TE = [], [], [], [], [], []
Ground_Truth_DE, LR_DE, DT_DE, RF_DE, SVM_DE, KNN_DE = [], [], [], [], [], []
Ground_Truth_IE, LR_IE, DT_IE, RF_IE, SVM_IE, KNN_IE = [], [], [], [], [], []
Ground_Truth_SE, LR_SE, DT_SE, RF_SE, SVM_SE, KNN_SE = [], [], [], [], [], []
Ground_Truth_EO1, LR_EO1, DT_EO1, RF_EO1, SVM_EO1, KNN_EO1 = [], [], [], [], [], []
Ground_Truth_EO2, LR_EO2, DT_EO2, RF_EO2, SVM_EO2, KNN_EO2 = [], [], [], [], [], []
path = r"Path"
for filename in listdir(path):
    full_path = join(path, filename)
    if isfile(full_path):
        df = pd.read_csv(full_path)
        
        #Statistical Parity
        SP = df["SP_Score"]
        Ground_Truth_SP.append(abs(SP[0]))
        LR_SP.append(abs(SP[1]))
        DT_SP.append(abs(SP[2]))
        RF_SP.append(abs(SP[3]))
        SVM_SP.append(abs(SP[4]))
        KNN_SP.append(abs(SP[5]))
        
        #Treatment Equality
        TE = df["TE_Score"]
        LR_TE.append(abs(TE[1]))
        DT_TE.append(abs(TE[2]))
        RF_TE.append(abs(TE[3]))
        SVM_TE.append(abs(TE[4]))
        KNN_TE.append(abs(TE[5]))
        
        # #Cft Direct Effect
        # DE = df["DE_Score"]
        # Ground_Truth_DE.append(abs(DE[0]))
        # LR_DE.append(abs(DE[1]))
        # DT_DE.append(abs(DE[2]))
        # RF_DE.append(abs(DE[3]))
        # SVM_DE.append(abs(DE[4]))
        # KNN_DE.append(abs(DE[5]))
        
        # #Cft Indirect Effect
        # IE = df["IE_Score"]
        # Ground_Truth_IE.append(abs(IE[0]))
        # LR_IE.append(abs(IE[1]))
        # DT_IE.append(abs(IE[2]))
        # RF_IE.append(abs(IE[3]))
        # SVM_IE.append(abs(IE[4]))
        # KNN_IE.append(abs(IE[5]))
        
        # #Cft Indirect Effect
        # SE = df["SE_Score"]
        # Ground_Truth_SE.append(abs(SE[0]))
        # LR_SE.append(abs(SE[1]))
        # DT_SE.append(abs(SE[2]))
        # RF_SE.append(abs(SE[3]))
        # SVM_SE.append(abs(SE[4]))
        # KNN_SE.append(abs(SE[5]))
        
        #Equalised Odds
        EO = df["EO_Score"]
        LR_EO1.append(abs(float(EO[1].split(",")[0][1:])))
        DT_EO1.append(abs(float(EO[2].split(",")[0][1:])))
        RF_EO1.append(abs(float(EO[3].split(",")[0][1:])))
        SVM_EO1.append(abs(float(EO[4].split(",")[0][1:])))
        KNN_EO1.append(abs(float(EO[5].split(",")[0][1:])))
        
        LR_EO2.append(abs(float(EO[1].split(",")[1][1:-1])))
        DT_EO2.append(abs(float(EO[2].split(",")[1][1:-1])))
        RF_EO2.append(abs(float(EO[3].split(",")[1][1:-1])))
        SVM_EO2.append(abs(float(EO[4].split(",")[1][1:-1])))
        KNN_EO2.append(abs(float(EO[5].split(",")[1][1:-1])))
        
        




plt.boxplot(Ground_Truth_SP, widths=0.5)
plt.boxplot(LR_SP, positions=[2], widths=0.5)
plt.boxplot(DT_SP, positions=[3], widths=0.5)
plt.boxplot(RF_SP, positions=[4], widths=0.5)
plt.boxplot(SVM_SP, positions=[5], widths=0.5)
plt.boxplot(KNN_SP, positions=[6], widths=0.5)
plt.xticks([1,2,3,4,5,6],["Input Data","Logistic Regression", "Decision Tree", "Random Forest", "Support Vector Machine", 
                          "K Nearest Neighbours"], rotation = 45, ha="right")
plt.xlabel("Model")
plt.ylabel("Statistical Parity Score")
plt.title("High Parity Group")
plt.show()

#plt.boxplot(Ground_Truth_TE, widths=0.5)
plt.boxplot(LR_TE, positions=[1], widths=0.5)
plt.boxplot(DT_TE, positions=[2], widths=0.5)
plt.boxplot(RF_TE, positions=[3], widths=0.5)
plt.boxplot(SVM_TE, positions=[4], widths=0.5)
plt.boxplot(KNN_TE, positions=[5], widths=0.5)
plt.xticks([1,2,3,4,5],["Logistic Regression", "Decision Tree", "Random Forest", "Support Vector Machine", 
                        "K Nearest Neighbours"], rotation = 45, ha="right")
plt.xlabel("Model")
plt.ylabel("Treatment Equality Score")
#plt.ylim(0,3)
plt.title("High Parity Group")
plt.show()




plt.boxplot(LR_EO1, positions=[1], widths=0.5)
plt.boxplot(DT_EO1, positions=[2], widths=0.5)
plt.boxplot(RF_EO1, positions=[3], widths=0.5)
plt.boxplot(SVM_EO1, positions=[4], widths=0.5)
plt.boxplot(KNN_EO1, positions=[5], widths=0.5)
plt.xticks([1,2,3,4,5],["Logistic Regression", "Decision Tree",
                                   "Random Forest","Support Vector Machine",  
                                   "K Nearest Neighbours",], rotation = 45, ha="right")
plt.xlabel("Model")
plt.ylabel("Equalised Odds Score, y=0")
#plt.ylim(0,0.6)
plt.title("High Parity Group")
plt.show()


plt.boxplot(LR_EO2, positions=[1], widths=0.5)
plt.boxplot(DT_EO2, positions=[2], widths=0.5)
plt.boxplot(RF_EO2, positions=[3], widths=0.5)
plt.boxplot(SVM_EO2, positions=[4], widths=0.5)
plt.boxplot(KNN_EO2, positions=[5], widths=0.5)
plt.xticks([1,2,3,4,5],["Logistic Regression", "Decision Tree",
                                   "Random Forest","Support Vector Machine",  
                                   "K Nearest Neighbours",], rotation = 45, ha="right")
plt.xlabel("Model")
plt.ylabel("Equalised Odds Score, y=1")
#plt.ylim(0,0.6)
plt.title("High Parity Group")
plt.show()

#ANOVA tests
from scipy.stats import ttest_ind, ttest_rel, ranksums
import statsmodels.stats.multitest as smm

p1=ranksums(Ground_Truth_SP, LR_SP)[1]
p2=ranksums(Ground_Truth_SP, DT_SP)[1]
p3=ranksums(Ground_Truth_SP, RF_SP)[1]
p4=ranksums(Ground_Truth_SP, SVM_SP)[1]
p5=ranksums(Ground_Truth_SP, KNN_SP)[1]
p6=ranksums(LR_SP, DT_SP)[1]
p7=ranksums(LR_SP, RF_SP)[1]
p8=ranksums(LR_SP, SVM_SP)[1]
p9=ranksums(LR_SP, KNN_SP)[1]
p10=ranksums(DT_SP, RF_SP)[1]
p11=ranksums(DT_SP, SVM_SP)[1]
p12=ranksums(DT_SP, KNN_SP)[1]
p13=ranksums(RF_SP, SVM_SP)[1]
p14=ranksums(RF_SP, KNN_SP)[1]
p15=ranksums(SVM_SP, KNN_SP)[1]

results1 = smm.multipletests([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15],alpha=0.05,method='fdr_bh')[1]

p6=ranksums(LR_TE, DT_TE)[1]
p7=ranksums(LR_TE, RF_TE)[1]
p8=ranksums(LR_TE, SVM_TE)[1]
p9=ranksums(LR_TE, KNN_TE)[1]
p10=ranksums(DT_TE, RF_TE)[1]
p11=ranksums(DT_TE, SVM_TE)[1]
p12=ranksums(DT_TE, KNN_TE)[1]
p13=ranksums(RF_TE, SVM_TE)[1]
p14=ranksums(RF_TE, KNN_TE)[1]
p15=ranksums(SVM_TE, KNN_TE)[1]

results2 = smm.multipletests([p6,p7,p8,p9,p10,p11,p12,p13,p14,p15],alpha=0.05,method='fdr_bh')[1]

p6=ranksums(LR_EO1, DT_EO1)[1]
p7=ranksums(LR_EO1, RF_EO1)[1]
p8=ranksums(LR_EO1, SVM_EO1)[1]
p9=ranksums(LR_EO1, KNN_EO1)[1]
p10=ranksums(DT_EO1, RF_EO1)[1]
p11=ranksums(DT_EO1, SVM_EO1)[1]
p12=ranksums(DT_EO1, KNN_EO1)[1]
p13=ranksums(RF_EO1, SVM_EO1)[1]
p14=ranksums(RF_EO1, KNN_EO1)[1]
p15=ranksums(SVM_EO1, KNN_EO1)[1]

results3 = smm.multipletests([p6,p7,p8,p9,p10,p11,p12,p13,p14,p15],alpha=0.05,method='fdr_bh')[1]

p6=ranksums(LR_EO2, DT_EO2)[1]
p7=ranksums(LR_EO2, RF_EO2)[1]
p8=ranksums(LR_EO2, SVM_EO2)[1]
p9=ranksums(LR_EO2, KNN_EO2)[1]
p10=ranksums(DT_EO2, RF_EO2)[1]
p11=ranksums(DT_EO2, SVM_EO2)[1]
p12=ranksums(DT_EO2, KNN_EO2)[1]
p13=ranksums(RF_EO2, SVM_EO2)[1]
p14=ranksums(RF_EO2, KNN_EO2)[1]
p15=ranksums(SVM_EO2, KNN_EO2)[1]

results4 = smm.multipletests([p6,p7,p8,p9,p10,p11,p12,p13,p14,p15],alpha=0.05,method='fdr_bh')[1]

