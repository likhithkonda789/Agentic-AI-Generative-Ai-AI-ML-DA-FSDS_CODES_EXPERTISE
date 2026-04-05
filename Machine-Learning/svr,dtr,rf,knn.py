import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\LIKHITH\OneDrive\Desktop\Data science\Data_files\emp_sal.csv")

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values 

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y) 

# linear regression visualizaton 
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Linear Regression graph')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

lin_model_pred = lin_reg.predict([[6.5]])
print(lin_model_pred)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 5)
X_poly = poly_reg.fit_transform(X) 

poly_reg.fit(X_poly, y) 

lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)


plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print(poly_model_pred)

# SVR MODEL 
from sklearn.svm import SVR
svr_regressor = SVR(kernel='poly',degree=4, C=5, gamma='auto') 
svr_regressor.fit(X, y)

svr_pred = svr_regressor.predict([[6.5]])
print(svr_pred)


# KNN Model
from sklearn.neighbors import KNeighborsRegressor
knn_reg = KNeighborsRegressor(n_neighbors=2, weights='distance', algorithm='brute')
knn_reg.fit(X,y)

knn_pred = knn_reg.predict([[6.5]])
print(knn_pred) 


# Decission Tree 
from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor(criterion='poisson', max_depth=3, random_state=0)
dt_reg.fit(X,y)

dt_pred = dt_reg.predict([[6.5]])
print(dt_pred)        

# Random Forest Algorithm 
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators=20, random_state=43)
rf_reg.fit(X,y)

rf_pred = rf_reg.predict([[6.5]])
print(rf_pred)






      



            
    

 








