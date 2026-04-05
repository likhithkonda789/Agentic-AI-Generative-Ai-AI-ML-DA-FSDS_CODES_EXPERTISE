import numpy as np 	#Array		
import matplotlib.pyplot as plt		
import pandas as pd	
dataset = pd.read_csv(r"C:\Users\LIKHITH\OneDrive\Documents\Salary_Data.csv")

x = dataset.iloc[:, :-1].values	
y = dataset.iloc[:,-1].values 

from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=0)

from sklearn.linear_model import LinearRegression 
regresser = LinearRegression()
regresser.fit(x_train, y_train)

y_pred = regresser.predict(x_test)

plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_train, regresser.predict(x_train), color ='blue')
plt.title('salary vs Experiance (Test set')
plt.xlabel('years of Experiance')
plt.ylabel('salary')
plt.show()

m_slope = regresser.coef_
print(m_slope)

c_intercept = regresser.intercept_
print(c_intercept)

y_20 = m_slope * 20+c_intercept
print(y_20)

bias_score = regresser.score(x_train , y_train)
print(bias_score)

variance_score = regresser.score(x_test , y_test)
print(variance_score)


 # Lets implement stats to ml

dataset.mean() 
dataset['Salary'].mean()
dataset['YearsExperience'].mean()

dataset.median() 
dataset['Salary'].median()
dataset['YearsExperience'].median()

dataset.mode() 
dataset['Salary'].mode()
dataset['YearsExperience'].mode()



dataset.var()
dataset['Salary'].var()
dataset['YearsExperience'].var()

dataset.std()
dataset['Salary'].std()
dataset['YearsExperience'].std()


from scipy.stats import variation
variation(dataset.values)
variation(dataset['Salary'])
variation(dataset['YearsExperience'])

dataset.corr()

dataset['Salary'].corr(dataset['YearsExperience'])
dataset['Salary'].corr(dataset['Salary'])

dataset.skew()
# standard error

dataset.sem()
# Z-score
import scipy.stats as stats
dataset.apply(stats.zscore)

stats.zscore(dataset['Salary']) 
stats.zscore(dataset['YearsExperience']) 

# ANOVA

# ssr
y_mean=np.mean(y) 
SSR = np.sum((y_pred-y_mean)**2)
print(SSR)

#sse
y=y[0:6]
SSE=np.sum((y-y_pred)**2)
print(SSE)

#sst
mean_total = np.mean(dataset.values)
# here df.to_numpy()will convert pandas Dataframe to Nump
SST=np.sum((dataset.values-mean_total)**2)
print(SST)

r_square = 1 - (SSR / SST)
r_square

print(r_square)
print(bias_score)
print(variance_score) 

import pickle
filename = 'linear_regression_model.pkl'

with open(filename, 'wb') as file:
    pickle.dumb(regresser, file)
print("model has been pickled and saved as linear_regression_model")











