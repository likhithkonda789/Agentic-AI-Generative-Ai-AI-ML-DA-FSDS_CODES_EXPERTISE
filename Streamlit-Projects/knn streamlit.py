import streamlit as st
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

st.title("KNN Classification – Streamlit App")

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    dataset = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(dataset.head())

    # Features and target (same as your code)
    X = dataset.iloc[:, [2, 3]].values
    y = dataset.iloc[:, -1].values

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=0
    )

    # Scaling
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Select K
    k = st.slider("Select number of neighbors (K)", 1, 15, 5)

    # KNN Model
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(X_train, y_train)

    # Predictions
    y_pred = classifier.predict(X_test)

    # Metrics
    cm = confusion_matrix(y_test, y_pred)
    ac = accuracy_score(y_test, y_pred)
    cr = classification_report(y_test, y_pred)

    bias = classifier.score(X_train, y_train)
    variance = classifier.score(X_test, y_test)

    # Output
    st.subheader("Confusion Matrix")
    st.write(cm)

    st.subheader("Accuracy")
    st.write(ac)

    st.subheader("Classification Report")
    st.text(cr)

    st.subheader("Bias & Variance")
    st.write(f"Training Accuracy (Bias): {bias}")
    st.write(f"Testing Accuracy (Variance): {variance}")
