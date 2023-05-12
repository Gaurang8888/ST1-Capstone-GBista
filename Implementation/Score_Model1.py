#Submitted as part of ST1 Capstone Project
#Author: Gaurang Bista
#12/05/2023


#Import neccessary libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy
from numpy import arange
from matplotlib import pyplot
from pandas import read_csv
from pandas import set_option
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
import sklearn
import numpy as np
#from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
#from sklearn.linear_model import LogisticRegression
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier


#Read datafile
df = pd.read_csv('CapstoneDATAPREP.csv')
#Assign dataset to the train and test variables
train = pd.read_csv('CapstoneDATAPREP.csv')
test = pd.read_csv('CapstoneDATAPREP.csv')

#Determine features to be used
features = ['age', 'sex', 'graduated_h_school_type',
       'scholarship_type', 'additional_work', 'activity', 'partner',
       'total_salary', 'transport', 'accomodation', 'mother_ed', 'farther_ed',
       'weekly_study_hours', 'reading_non_scientific', 'reading_scientific',
       'attendance_seminars_dep', 'impact_of_projects', 'attendances_classes',
       'preparation_midterm_company', 'preparation_midterm_time',
       'taking_notes', 'listenning', 'discussion_improves_interest',
       'flip_classrom', 'grade_previous']
x_train = train[list(features)].values
y_train = train["grade"].values
x_test = test[list(features)].values
y = list('grade')
num_folds = 10
seed = 7
scoring = "accuracy"

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x_train, y_train, test_size = 0.20, random_state=seed)

np.shape(x_train), np.shape(x_test)

#Test each Model for the accuracy ratings
models = []
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
models.append(('GBM', GradientBoostingClassifier()))
models.append(('RF', RandomForestClassifier()))
# evaluate each model in turn
results = []
names = []
print("Accuracy Rates on Training set")
for name, model in models:
  kfold = KFold(n_splits=num_folds,shuffle=True,random_state=seed)
  cv_results = cross_val_score(model, x_train, y_train, cv=kfold, scoring= 'accuracy')
  results.append(cv_results)
  names.append(name)
  msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
  msg += '\n'
  print(msg)

rf = RandomForestClassifier(n_estimators = 10)
rf.fit(x_train, y_train)
sur = rf.predict(x_test)

best_model = rf
best_model.fit(x_train, y_train)

for x in range(len(sur)):
  print("Predicted: ", sur[x], "Actual: ", y_train[x], "Data: ", x_test[x])