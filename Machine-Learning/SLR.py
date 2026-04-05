# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# Load the dataset
dataset = pd.read_csv(r"C:\Users\LIKHITH\OneDrive\Desktop\Data science\Data_files\Salary_Data.csv")
# Check the shape of the dataset
print("Dataset Shape:", dataset.shape)  # (30, 2)

# Feature selection (independent variable X and dependent variable y)
x = dataset.iloc[:, :-1]  # Years of experience (Independent variable)
y = dataset.iloc[:, -1]   # Salary (Dependent variable)

# Split the dataset into training and testing sets (80% training, 20% testing)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=0)

# Reshape x_train and x_test into 2D arrays if they are single feature columns
x_train = x_train.values.reshape(-1, 1)
x_test = x_test.values.reshape(-1, 1)

# You don't need to reshape y_train, as it's the target variable
# Fit the Linear Regression model to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Predicting the results for the test set
y_pred = regressor.predict(x_test)

# Visualizing the Training set results
plt.scatter(x_train, y_train, color = 'red')  # Real salary data (training)
plt.plot(x_train, regressor.predict(x_train), color = 'blue')  # Predicted regression line
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualizing the Test set results
plt.scatter(x_test, y_test, color = 'red')  # Real salary data (testing)
plt.plot(x_train, regressor.predict(x_train), color = 'blue')  # Regression line from training set
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Optional: Output the coefficients of the linear model
print(f"Intercept: {regressor.intercept_}")
print(f"Coefficient: {regressor.coef_}")


bias = regressor.score(x_train, y_train)
print(bias)

variance = regressor.score(x_test,y_test)
print(variance)


# stats for ml 


# Compare predicted and actual salaries from the test set
comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison)

#STATISTICS FOR MACHINE LEARNING

dataset.mean()

dataset['Salary'].mean() 

dataset.median() 

dataset['Salary'].mode()

dataset.describe()

dataset.var() 

dataset.std()

dataset.corr()


# ssr 
y_mean = np.mean(y)
SSR = np.sum((y_pred-y_mean)**2)
print(SSR)

#sse
y = y[0:6]
SSE = np.sum((y-y_pred)**2)
print(SSE)

#sst 
mean_total = np.mean(dataset.values) # here df.to_numpy()will convert pandas Dataframe to Nump
SST = np.sum((dataset.values-mean_total)**2)
print(SST)

#r2 
r_square = 1 - SSR/SST
print(r_square)


bias = regressor.score(x_train, y_train)
print(bias)

variance = regressor.score(x_test, y_test)
print(variance)


# Predict salary for 12 and 20 years of experience using the trained model
y_12 = regressor.predict([[12]])
y_20 = regressor.predict([[20]])
print(f"Predicted salary for 12 years of experience: ${y_12[0]:,.2f}")
print(f"Predicted salary for 20 years of experience: ${y_20[0]:,.2f}")


from sklearn.metrics import r2_score,mean_squared_error

# Check model performance
bias = regressor.score(x_train, y_train)
variance = regressor.score(x_test, y_test)
train_mse = mean_squared_error(y_train, regressor.predict(x_train))
test_mse = mean_squared_error(y_test, y_pred)

print(f"Training Score (R^2): {bias:.2f}")
print(f"Testing Score (R^2): {variance:.2f}")
print(f"Training MSE: {train_mse:.2f}")
print(f"Test MSE: {test_mse:.2f}")


# Save the trained model to disk
filename = 'linear_regression_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(regressor, file)
print("Model has been pickled and saved as linear_regression_model.pkl") 

import os 
print(os.getcwd())




R2=r2_score(y_test,y_pred)
MSE=mean_squared_error(y_test,y_pred)
#MSE**(1/2)
RMSE=np.sqrt(MSE)
#accuracy_score(y_test,y_predictions) # it is a regression tech
print("R-sqaure:",R2)
print("MSE:",MSE)
print("RMSE:",RMSE)

#regression table code
# introduce to OLS & stats.api
from statsmodels.api import OLS
OLS(y_train,x_train).fit().summary()