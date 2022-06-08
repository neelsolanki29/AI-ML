# -*- coding: utf-8 -*-
"""Cardiac Arrest Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RylG-f-oP0S60hBDXyElV_US5OjRLjik

# Basic Data Analysis
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re

'''Database:           0   1   2   3   4 Total
          Cleveland: 164  55  36  35  13   303
          Hungarian: 188  37  26  28  15   294
        Switzerland:   8  48  32  30   5   123
      Long Beach VA:  51  56  41  42  10   200 '''

n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m

rf= open('processed.cleveland.data', 'r', encoding='cp1252') # read a file
cf=open('puran1.txt','w',encoding='cp1252') # creat a new empty file


n = 303
m = 14
hd1 = [0] * n
#for i in range(n):
    #print(hd[i])

for i in range(n):
    hd1[i] = [0] * m
i=0
j=0
for line in rf: 
    for word in line.split(","):
        world=word.rstrip('\n')
        world = re.sub('[?]', '0', world)
        hd1[i][j]=float(world)
        print("value i: "+str(i)+"  val j"+str(j)+" "+world)
        j=j+1
       
    i=i+1
    j=0

#nf=open('puran1.txt','r',encoding='cp1252')
#df=pd.Dataframe()


#content=nf.read()
#print(content)
#print(nf.seek(0))

#df=pd.read_csv('C:\\Users\\P Singh\\Desktop\\project_data\\data.csv')
#pd.DataFrame(df).head()
#rf= open('C:\\Users\\P Singh\\Desktop\\project_data\\ProcessedData.txt', 'r', encoding='cp1252') # read a file
rf= open('LongBeach.txt', 'r', encoding='cp1252') # read a file
n = 200
m = 75
hd3 = [0] * n
#for i in range(n):
    #print(hd[i])

for i in range(n):
    hd3[i] = [0] * m
i=0
j=0
for line in rf: 
    cf.write(line) # copy in empty file using write command
    
    for word in line.split():
        if word=="name":
             break
        print("value i: "+str(i)+"  val j"+str(j)+" "+word)
        hd3[i][j]=float(word)
        j=j+1
    if word=="name":    
        i=i+1
        j=0

rf= open('switzerland.txt', 'r', encoding='cp1252') # read a file
cf=open('puran1.txt','w',encoding='cp1252') # creat a new empty file


n = 123
m = 14
hd2 = [0] * n
#for i in range(n):
    #print(hd[i])

for i in range(n):
    hd2[i] = [0] * m
i=0
j=0
for line in rf: 
    for word in line.split(","):
        world=word.rstrip('\n')
        world = re.sub('[?]', '-9', world)
        hd2[i][j]=float(world)
        print("value i: "+str(i)+"  val j"+str(j)+" "+world)
        j=j+1
       
    i=i+1
    j=0

#nf=open('puran1.txt','r',encoding='cp1252')
#df=pd.Dataframe()


#content=nf.read()
#print(content)
#print(nf.seek(0))

df2=pd.DataFrame(hd2)
colm=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak' ,'slope','ca','thal' ,'diagnosis']

df2.columns=colm
df2.tail(20)

rf= open('hungerian.txt', 'r', encoding='cp1252') # read a file
cf=open('puran1.txt','w',encoding='cp1252') # creat a new empty file


n = 294
m = 14
hd4 = [0] * n
#for i in range(n):
    #print(hd[i])

for i in range(n):
    hd4[i] = [0] * m
i=0
j=0
for line in rf: 
    for word in line.split(" "):
        world=word.rstrip('\n')
        world = re.sub('[?]', '-9', world)
        hd4[i][j]=float(world)
        print("value i: "+str(i)+"  val j"+str(j)+" "+world)
        j=j+1
       
    i=i+1
    j=0

#nf=open('puran1.txt','r',encoding='cp1252')
#df=pd.Dataframe()


#content=nf.read()
#print(content)
#print(nf.seek(0))

import re
stre = "hello </789 gt6? 5&67_m buddy?007"
my_new_string = re.sub('[^0-9]', '', stre)
print(my_new_string)

df4=pd.DataFrame(hd4)
colm=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak' ,'slope','ca','thal' ,'diagnosis']

df4.columns=colm
df4.tail(20)

df1=pd.DataFrame(hd1)
df1

len(df1)

colm=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak' ,'slope','ca','thal' ,'diagnosis']

df1.columns=colm
df1.head()

corelation = df1.corr()
cmap = sns.diverging_palette(220, 10, as_cmap = True)
f, ax = plt.subplots(figsize = (16, 12))
sns.heatmap(corelation,annot=True ,cmap=cmap,linewidths=1 ,linecolor='black')

df3=pd.DataFrame(hd3)
df3.tail()

df3=df3.iloc[:,[2,3,8,9,11,15,18,31,37,39,40,43,50,57]]

df3.tail()

type(df3)

df3.columns

colm=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak' ,'slope','ca','thal' ,'diagnosis']

df3.columns=colm

df3

sns.countplot(x='diagnosis',data=df3)

df_x_2=df2.drop('diagnosis',axis=1)
df_y_2=df2['diagnosis']
df_y_2=df_y_2.astype("int")
df_y_2=df_y_2.replace([2,3,4],1)
df_y_2

df_x_4=df4.drop('diagnosis',axis=1)
df_y_4=df4['diagnosis']
df_y_4=df_y_4.astype("int")
df_y_4=df_y_4.replace([2,3,4],1)
df_y_4

df_x_3=df3.drop('diagnosis',axis=1)
df_y_3=df3['diagnosis']
df_y_3=df_y_3.astype("int")
df_y_3=df_y_3.replace([2,3,4],1)
df_y_3

sns.countplot(x=df_y_4)

df_x_1=df1.drop(['diagnosis'],axis=1)
df_x_1.head()

df_y_1=df1['diagnosis']
df_y_1=df_y_1.astype("int")
df_y_1

df_y_1=df_y_1.replace([2,3,4],1)
df_y_1

sns.countplot(x=df_y_1)

df_x=pd.concat([df_x_1,df_x_3,df_x_2,df_x_4],ignore_index=True)
df_x_new=pd.concat([df1,df3,df2,df4],ignore_index=True)
df_x_new.head()

df=df_x_new.replace([-9,-9.0], np.NaN)
df.isnull().sum()

sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap="viridis")

#df.drop(['ca', 'thal'],axis=1,inplace=True)
sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap="viridis")

np.mean(df['slope'])

from scipy import stats

lst1=df['slope']
stats.mode(lst1)

np.median(df['slope'])

df['slope']=df['slope'].fillna(2)
df['chol']=df['chol'].fillna(np.mean(df['chol']))
df['fbs']=df['fbs'].fillna(0)
df['restecg']=df['restecg'].fillna(0)

#df['ca']=df['ca'].fillna(0,filter(lambda item:item==0,df['diagnosis']))

#for treating df['ca']
df['ca']=df['ca'].fillna(-9)
for i in range(0,len(df)):
    if df['diagnosis'][i]==0:
        if df['ca'][i]==-9:
            df['ca'][i]=0
    else:
        if df['ca'][i]==-9:
            df['ca'][i]=2;

#for treating df['thal']
df['thal']=df['thal'].fillna(-9)
for i in range(0,len(df)):
    if df['diagnosis'][i]==0:
        if df['thal'][i]==-9:
            df['thal'][i]=3
    else:
        if df['thal'][i]==-9:
            df['thal'][i]=7;



df.dropna(subset=['trestbps','thalach','exang', 'oldpeak','slope'],axis=0,inplace=True)
sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap="viridis")

df.isnull().sum()

len(df)

dftemp=df.abs()

temp=dftemp['oldpeak']
dftemp=dftemp[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'slope', 'ca', 'thal', 'diagnosis']].astype('int')
dftemp['oldpeak']=temp
len(dftemp)

dftemp.isnull().sum()

df.to_csv("C:\\Users\\91942\\Desktop\\PhD\\My 3rd Paper\\heart-disease dataset\\Heart_Disease_dataSet1.csv",index=False)

sns.countplot(x="diagnosis",hue="chol", data=df1)

df_x_=dftemp.drop("diagnosis",axis=1)
df_x_["chol"].loc[500:520]

df_y_=dftemp['diagnosis']
df_y_=df_y_.astype("int")
df_y_=df_y_.replace([2,3,4],1)

sns.countplot(x=df_y_)

len(df_y_)

#df_y=pd.concat([df_y_1,df_y_3,df_y_2,df_y_4],ignore_index=True)
#df_y

from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test= train_test_split(df_x_,df_y_,test_size=0.25,random_state=3)
y_test.shape

sns.distplot(df['age'])

sns.distplot(df['trestbps'])

sns.distplot(df['chol'])

sns.distplot(df['thalach'])

df.duplicated()

"""## Feature Selection


"""

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

df.shape

### Apply SelectKBest Algorithm
ordered_rank_features=SelectKBest(score_func=chi2,k=13)
ordered_feature=ordered_rank_features.fit(df_x_,df_y_)

dfscores=pd.DataFrame(ordered_feature.scores_,columns=["Score"])
dfcolumns=pd.DataFrame(df_x_.columns)

features_rank=pd.concat([dfcolumns,dfscores],axis=1)

features_rank.columns=['Features','Score']
features_rank

features_rank.nlargest(13,'Score')

"""### Feature Importance

"""

from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
model=ExtraTreesClassifier()
model.fit(df_x_,df_y_)

print(model.feature_importances_)

ranked_features=pd.Series(model.feature_importances_,index=df_x_.columns)
ranked_features.nlargest(13).plot(kind='barh')
plt.show()





"""# Logistic Regression"""

from sklearn.linear_model import LogisticRegression
lg= LogisticRegression()

lg.fit(x_train,y_train)

lg.score(x_train,y_train)

pred=lg.predict(x_test)

from sklearn import metrics
metrics.accuracy_score(y_test, pred)

metrics.confusion_matrix(y_test,pred)

from sklearn.metrics import cohen_kappa_score
cohen_kappa_score(y_test, pred)

from sklearn.metrics import classification_report
pred=lg.predict(x_test)
print(classification_report(y_test, pred))

from sklearn import metrics
import matplotlib.pyplot as plt

y_pred_proba = lg.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)

plt.plot(fpr,tpr)
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

y_pred_proba = lg.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)

plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.show()

from sklearn.metrics import PrecisionRecallDisplay

display = PrecisionRecallDisplay.from_estimator(lg, x_test, y_test, name="Logistic Regression")
_ = display.ax_.set_title("2-class Precision-Recall curve")

#Making confusion matrix
from sklearn.metrics import confusion_matrix
cm1 = confusion_matrix(y_test,pred)
print(cm1)
sensitivity1 = cm1[0,0]/(cm1[0,0]+cm1[0,1])
print('Sensitivity : ', sensitivity1 )

specificity1 = cm1[1,1]/(cm1[1,0]+cm1[1,1])
print('Specificity : ', specificity1)

"""# SVM"""

from sklearn import svm

sm=svm.SVC(C=1,gamma=1,kernel='linear')
sm.fit(x_train,y_train)

pred1=sm.predict(x_test)
metrics.accuracy_score(y_test, pred1)

metrics.confusion_matrix(y_test,pred1)

from sklearn.metrics import cohen_kappa_score
cohen_kappa_score(y_test, pred)

from sklearn.metrics import classification_report
pred=sm.predict(x_test)
print(classification_report(y_test, pred))

from sklearn.metrics import PrecisionRecallDisplay

display = PrecisionRecallDisplay.from_estimator(sm, x_test, y_test, name="Support Vector Machine")
_ = display.ax_.set_title("2-class Precision-Recall curve")

#Making confusion matrix
from sklearn.metrics import confusion_matrix
cm1 = confusion_matrix(y_test,pred)
print(cm1)
sensitivity1 = cm1[0,0]/(cm1[0,0]+cm1[0,1])
print('Sensitivity : ', sensitivity1 )

specificity1 = cm1[1,1]/(cm1[1,0]+cm1[1,1])
print('Specificity : ', specificity1)

"""# NeuraL Network"""

from sklearn.neural_network import MLPClassifier

MLNN=MLPClassifier(solver='lbfgs',activation='relu',alpha=10,hidden_layer_sizes=(15,5),random_state=1)

MLNN.fit(x_train,y_train)

NN_pred=MLNN.predict(x_test)

metrics.accuracy_score(NN_pred,y_test)

metrics.confusion_matrix(NN_pred,y_test)







"""# Dimensionality Reduction[PCA]"""

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

std=StandardScaler()
x_df_new=std.fit_transform(df_x)

x_train1, x_test1,y_train1, y_test1= train_test_split(df_x_,df_y_,test_size=0.25,random_state=3)

pca_heart=PCA(.99)

pca_heart.fit(x_train1)

pca_heart.n_components_

new_train=pca_heart.transform(x_train1)
new_test=pca_heart.transform(x_test1)



from sklearn.neural_network import MLPClassifier

from sklearn.neural_network import MLPClassifier

MLNN1=MLPClassifier(solver='lbfgs',activation='relu',alpha=10,hidden_layer_sizes=(7,3),random_state=1)

MLNN1.fit(new_train,y_train1)

pred_pca=MLNN1.predict(new_test)
from sklearn import metrics
metrics.accuracy_score(pred_pca,y_test1)

metrics.precision_recall_fscore_support(pred_pca,y_test1)

metrics.recall_score(pred_pca,y_test1)

metrics.confusion_matrix(pred_pca,y_test1)

"""# Random Forest"""

from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split
x_trainrf, x_testrf,y_trainrf, y_testrf= train_test_split(df_x_,df_y_,test_size=0.1,random_state=6)

RF=RandomForestClassifier(criterion='entropy',max_depth=5,n_estimators=60,n_jobs=-1,random_state=6) #random_state=0,1,2,3,5,6same

RF.fit(x_trainrf,y_trainrf)

RF_pred=RF.predict(x_testrf)

metrics.accuracy_score(RF_pred,y_testrf)

metrics.confusion_matrix(RF_pred,y_testrf)

x_train, x_test,y_train, y_test= train_test_split(df_x_,df_y_,test_size=0.2,random_state=42)
y_test.shape

"""# KNN Model"""

from sklearn.neighbors import KNeighborsClassifier
k=301
for k in range(301,400):
  classifier = KNeighborsClassifier(n_neighbors=k)
  classifier.fit(x_train,y_train)
  y_pred = classifier.predict(x_test)
  from sklearn.metrics import accuracy_score
  test_acc = accuracy_score(y_test,y_pred)
  acc_KNN = test_acc * 100
  print(k)
  print("Accuracy on test set = %0.3f"%acc_KNN)

"""x_train, x_test,y_train, y_test= train_test_split(df_x_,df_y_,test_size=0.25,random_state=3)
y_test.shape

# XG Boost Classifier
"""

from xgboost import XGBClassifier
model = XGBClassifier()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
metrics.accuracy_score(y_test, y_pred)

metrics.confusion_matrix(y_test,y_pred)

from sklearn.metrics import classification_report
pred=model.predict(x_test)
print(classification_report(y_test, pred))

from sklearn.metrics import cohen_kappa_score
cohen_kappa_score(y_test, y_pred)

from sklearn import metrics
import matplotlib.pyplot as plt

y_pred_proba = model.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)

plt.plot(fpr,tpr)
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

y_pred_proba = model.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)

plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.show()

from sklearn.metrics import PrecisionRecallDisplay

display = PrecisionRecallDisplay.from_estimator(model, x_test, y_test, name="XG Boost Classifier")
_ = display.ax_.set_title("2-class Precision-Recall curve")

#Making confusion matrix
from sklearn.metrics import confusion_matrix
cm1 = confusion_matrix(y_test,y_pred)
print(cm1)
sensitivity1 = cm1[0,0]/(cm1[0,0]+cm1[0,1])
print('Sensitivity : ', sensitivity1 )

specificity1 = cm1[1,1]/(cm1[1,0]+cm1[1,1])
print('Specificity : ', specificity1)

"""# Ada Boost Classifier"""

from sklearn.ensemble import AdaBoostClassifier
abc =AdaBoostClassifier(n_estimators=50, learning_rate=1)
model = abc.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.metrics import classification_report
pred=sm.predict(x_test)
print(classification_report(y_test, pred))

from sklearn.metrics import cohen_kappa_score
cohen_kappa_score(y_test, y_pred)

from sklearn import metrics
import matplotlib.pyplot as plt

y_pred_proba = model.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)

plt.plot(fpr,tpr)
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

y_pred_proba = model.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)

plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.title("ROC curve")
plt.show()

from sklearn.metrics import PrecisionRecallDisplay

display = PrecisionRecallDisplay.from_estimator(model, x_test, y_test, name="Ada Boost Classifier")
_ = display.ax_.set_title("2-class Precision-Recall curve")

#Making confusion matrix
from sklearn.metrics import confusion_matrix
cm1 = confusion_matrix(y_test,y_pred)
print(cm1)
sensitivity1 = cm1[0,0]/(cm1[0,0]+cm1[0,1])
print('Sensitivity : ', sensitivity1 )

specificity1 = cm1[1,1]/(cm1[1,0]+cm1[1,1])
print('Specificity : ', specificity1)

from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test= train_test_split(df_x_,df_y_,test_size=0.1,random_state=42)
y_test.shape

"""# Gradient Boost Classifier"""

from sklearn.ensemble import GradientBoostingClassifier
gbc=GradientBoostingClassifier(n_estimators=275,learning_rate=0.01,max_features=5)
gbc.fit(x_train,y_train)
print("GBC accuracy is %2.2f" % accuracy_score( 
     y_test, gbc.predict(x_test)))
from sklearn.metrics import classification_report
pred=gbc.predict(x_test)
print(classification_report(y_test, pred))

from sklearn.metrics import cohen_kappa_score
cohen_kappa_score(y_test, pred)

from sklearn import metrics
import matplotlib.pyplot as plt

y_pred_proba = gbc.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)

plt.plot(fpr,tpr)
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

y_pred_proba = gbc.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)

plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.show()

from sklearn.metrics import PrecisionRecallDisplay

display = PrecisionRecallDisplay.from_estimator(gbc, x_test, y_test, name="Gradient Boost Classifier")
_ = display.ax_.set_title("2-class Precision-Recall curve")

#Making confusion matrix
from sklearn.metrics import confusion_matrix
cm1 = confusion_matrix(y_test,pred)
print(cm1)

sensitivity1 = cm1[0,0]/(cm1[0,0]+cm1[0,1])
print('Sensitivity : ', sensitivity1 )

specificity1 = cm1[1,1]/(cm1[1,0]+cm1[1,1])
print('Specificity : ', specificity1)

x_train = x_train.values
y_train = y_train.values
x_test = x_test.values
y_test = y_test.values

# Commented out IPython magic to ensure Python compatibility.
# %pip install mlxtend --upgrade
from mlxtend.evaluate import bias_variance_decomp

# Bias Variance Tradeoff

mse, bias, var = bias_variance_decomp(model, x_train, y_train, x_test, y_test, loss='mse', num_rounds=200, random_seed=1)
print('MSE: %.3f' % mse)
print('Bias: %.3f' % bias)
print('Variance: %.3f' % var)

"""# Naive Bayes"""

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train,y_train)
y_pred = classifier.predict(x_test)
test_acc = accuracy_score(y_test,y_pred)
acc_NB = test_acc * 100
print("Accuracy on test set = %0.3f"%acc_NB)

from sklearn.metrics import classification_report
pred=gbc.predict(x_test)
print(classification_report(y_test, y_pred))

from sklearn import metrics
import matplotlib.pyplot as plt

y_pred_proba = classifier.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)

plt.plot(fpr,tpr)
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

y_pred_proba = classifier.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)

plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.show()

from sklearn.metrics import PrecisionRecallDisplay

display = PrecisionRecallDisplay.from_estimator(classifier, x_test, y_test, name="Naive Bayes")
_ = display.ax_.set_title("2-class Precision-Recall curve")

from sklearn.metrics import cohen_kappa_score
cohen_kappa_score(y_test, y_pred)

#Making confusion matrix
from sklearn.metrics import confusion_matrix
cm1 = confusion_matrix(y_test,y_pred)
print(cm1)
sensitivity1 = cm1[0,0]/(cm1[0,0]+cm1[0,1])
print('Sensitivity : ', sensitivity1 )

specificity1 = cm1[1,1]/(cm1[1,0]+cm1[1,1])
print('Specificity : ', specificity1)