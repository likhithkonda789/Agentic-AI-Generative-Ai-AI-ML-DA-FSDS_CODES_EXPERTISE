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

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
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
bias

variance = classifier.score(X_test, y_test)
variance


# -----------------------------
# Read data
# -----------------------------
dataset1 = pd.read_csv(r"C:\Users\LIKHITH\OneDrive\Desktop\Data science\final1.csv")

d2 = dataset1.copy()   # backup

# -----------------------------
# Encoding categorical columns
# -----------------------------
dataset1 = pd.get_dummies(d2.iloc[:, [2, 3]], drop_first=True)

# -----------------------------
# Scaling
# -----------------------------
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
M = sc.fit_transform(dataset1)

# -----------------------------
# Prediction
# -----------------------------
d2['y_pred'] = classifier.predict(M)

d2.to_csv('final1_prediction.csv', index=False)

# -----------------------------
# ROC – AUC
# -----------------------------
from sklearn.metrics import roc_auc_score, roc_curve
y_pred_prob = classifier.predict_proba(X_test)[:, 1]

auc_score = roc_auc_score(y_test, y_pred_prob)
print(auc_score)

fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

# -----------------------------
# Plot ROC Curve
# -----------------------------
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'Logistic Regression (AUC = {auc_score:.2f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.grid()
plt.show()


# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()