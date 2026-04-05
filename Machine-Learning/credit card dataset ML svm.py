# Support Vector Machine (SVM)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset (FIXED)
dataset = pd.read_excel(
    r"C:\Users\LIKHITH\OneDrive\Desktop\Data science\Data_files\default of credit card clients.xls",
    header=1
)

# X and y
X = dataset.iloc[:, 1:-1].values   # remove ID
y = dataset.iloc[:, -1].values

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=0
)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training SVM
from sklearn.svm import SVC
classifier = SVC(kernel='rbf',  C=10,
    gamma='auto', random_state=0)
classifier.fit(X_train, y_train)

# Prediction
y_pred = classifier.predict(X_test)

# Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Accuracy
from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print("Accuracy:", ac)

# Bias & Variance
bias = classifier.score(X_train, y_train)
variance = classifier.score(X_test, y_test)
print("Bias:", bias)
print("Variance:", variance)

# Classification Report
from sklearn.metrics import classification_report
cr = classification_report(y_test, y_pred)
print(cr)
