# -*- coding: utf-8 -*-
"""KNN_iris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rjCx99SFNQSuHo9AhPgcH8yQvv--eKmf
"""

import pandas as pd
from pandas import DataFrame

df_iris_db = pd.read_csv("/content/iris.data",header=None,index_col=None)

df_iris_db

x = df_iris_db.iloc[:, :-1].values
y = df_iris_db.iloc[:, 4].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x,y,train_size=0.8,random_state=100)
print(y_test)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train,y_train)

predicted= model.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, predicted))
print(classification_report(y_test, predicted))

result = model.predict([[5.9, 2.8, 6.0, 1.8]])
print(result)

