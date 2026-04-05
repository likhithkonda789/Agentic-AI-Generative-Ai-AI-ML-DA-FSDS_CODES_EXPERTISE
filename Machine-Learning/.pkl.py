import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Load CSV
data = pd.read_csv(r"C:\Users\LIKHITH\OneDrive\Documents\Salary_model.pkl.csv")

X = data[['YearsExperience']]
y = data['Salary']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model as pickle
with open(r"C:\Users\LIKHITH\OneDrive\Documents\salary_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")
