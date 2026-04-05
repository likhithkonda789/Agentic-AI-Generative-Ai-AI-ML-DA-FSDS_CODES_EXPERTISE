import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset =pd.read_csv(r"C:\Users\LIKHITH\OneDrive\Attachments\NIT(Data science)\DEC - 2025\logit classification.csv")

X = dataset.iloc[:,[2,3] ].values	
y = dataset.iloc[:, -1].values 

from sklearn.model_selection import train_test_split
X_train ,X_test, y_train ,y_test = train_test_split(X,y,test_size=0.20, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.svm import SVC
classifier = SVC(C = 1.0 , kernel="rbf")
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print(ac)

from sklearn.metrics import classification_report
cr = classification_report(y_test, y_pred)
print(cr)

bias = classifier.score(X_train, y_train)
print(bias)

variance = classifier.score(X_test, y_test)
print(variance)


