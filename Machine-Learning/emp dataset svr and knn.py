import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"C:\Users\LIKHITH\OneDrive\Attachments\NIT(Data science)\DEC - 2025\emp_sal.csv")

x = dataset.iloc[:, 1:2].values	
y = dataset.iloc[:, 2].values 

from sklearn.svm import SVR
regressor =  SVR(kernel='poly', degree=4 , gamma ='auto' , C=5.0)
regressor.fit(x,y)

from sklearn.neighbors import KNeighborsRegressor 
knn_reg = KNeighborsRegressor(n_neighbors =4, weights ='distance' , algorithm = 'kd_tree' , p= 1)
knn_reg.fit(x,y)

y_pred_knn = knn_reg.predict([[6.5]])
print(y_pred_knn)

y_pred_svr = regressor.predict([[6.5]])
print(y_pred_svr)

