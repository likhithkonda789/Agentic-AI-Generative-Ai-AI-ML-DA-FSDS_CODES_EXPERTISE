import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    classification_report,
    roc_auc_score,
    roc_curve
)
from matplotlib.colors import ListedColormap

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="Logistic Regression App", layout="wide")
st.title("📊 Logistic Regression Classification (Streamlit)")

# -----------------------------
# Upload dataset
# -----------------------------
st.sidebar.header("Upload Files")

train_file = st.sidebar.file_uploader(
    "Upload Training CSV (logit classification.csv)",
    type=["csv"]
)

predict_file = st.sidebar.file_uploader(
    "Upload Prediction CSV (final1.csv)",
    type=["csv"]
)

# -----------------------------
# Main Logic
# -----------------------------
if train_file is not None:

    dataset = pd.read_csv(train_file)
    st.subheader("🔍 Training Dataset Preview")
    st.dataframe(dataset.head())

    # -----------------------------
    # Feature selection
    # -----------------------------
    X = dataset.iloc[:, [2, 3]].values
    y = dataset.iloc[:, -1].values

    # -----------------------------
    # Train-test split
    # -----------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=0
    )

    # -----------------------------
    # Scaling
    # -----------------------------
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # -----------------------------
    # Model training
    # -----------------------------
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)

    # -----------------------------
    # Predictions
    # -----------------------------
    y_pred = classifier.predict(X_test)

    # -----------------------------
    # Metrics
    # -----------------------------
    cm = confusion_matrix(y_test, y_pred)
    acc = accuracy_score(y_test, y_pred)
    cr = classification_report(y_test, y_pred, output_dict=True)

    bias = classifier.score(X_train, y_train)
    variance = classifier.score(X_test, y_test)

    # -----------------------------
    # Display Metrics
    # -----------------------------
    st.subheader("📌 Model Performance")

    col1, col2, col3 = st.columns(3)
    col1.metric("Accuracy", f"{acc:.2f}")
    col2.metric("Bias (Train Score)", f"{bias:.2f}")
    col3.metric("Variance (Test Score)", f"{variance:.2f}")

    st.subheader("Confusion Matrix")
    st.write(cm)

    st.subheader("Classification Report")
    st.dataframe(pd.DataFrame(cr).transpose())

    # -----------------------------
    # ROC Curve
    # -----------------------------
    y_pred_prob = classifier.predict_proba(X_test)[:, 1]
    auc_score = roc_auc_score(y_test, y_pred_prob)

    fpr, tpr, _ = roc_curve(y_test, y_pred_prob)

    st.subheader("📈 ROC Curve")
    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, label=f"AUC = {auc_score:.2f}")
    ax.plot([0, 1], [0, 1], "k--")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.legend()
    ax.grid()
    st.pyplot(fig)

    # -----------------------------
    # Decision Boundary (Train)
    # -----------------------------
    st.subheader("🟢 Decision Boundary – Training Set")

    X_set, y_set = X_train, y_train
    X1, X2 = np.meshgrid(
        np.arange(X_set[:, 0].min() - 1, X_set[:, 0].max() + 1, 0.01),
        np.arange(X_set[:, 1].min() - 1, X_set[:, 1].max() + 1, 0.01)
    )

    fig, ax = plt.subplots()
    ax.contourf(
        X1,
        X2,
        classifier.predict(
            np.array([X1.ravel(), X2.ravel()]).T
        ).reshape(X1.shape),
        alpha=0.75,
        cmap=ListedColormap(("red", "green"))
    )

    for i, j in enumerate(np.unique(y_set)):
        ax.scatter(
            X_set[y_set == j, 0],
            X_set[y_set == j, 1],
            c=ListedColormap(("red", "green"))(i),
            label=j
        )

    ax.set_title("Logistic Regression (Training set)")
    ax.set_xlabel("Age")
    ax.set_ylabel("Estimated Salary")
    ax.legend()
    st.pyplot(fig)

    # -----------------------------
    # Decision Boundary (Test)
    # -----------------------------
    st.subheader("🔵 Decision Boundary – Test Set")

    X_set, y_set = X_test, y_test
    X1, X2 = np.meshgrid(
        np.arange(X_set[:, 0].min() - 1, X_set[:, 0].max() + 1, 0.01),
        np.arange(X_set[:, 1].min() - 1, X_set[:, 1].max() + 1, 0.01)
    )

    fig, ax = plt.subplots()
    ax.contourf(
        X1,
        X2,
        classifier.predict(
            np.array([X1.ravel(), X2.ravel()]).T
        ).reshape(X1.shape),
        alpha=0.75,
        cmap=ListedColormap(("red", "green"))
    )

    for i, j in enumerate(np.unique(y_set)):
        ax.scatter(
            X_set[y_set == j, 0],
            X_set[y_set == j, 1],
            c=ListedColormap(("red", "green"))(i),
            label=j
        )

    ax.set_title("Logistic Regression (Test set)")
    ax.set_xlabel("Age")
    ax.set_ylabel("Estimated Salary")
    ax.legend()
    st.pyplot(fig)

    # -----------------------------
    # Prediction on new file
    # -----------------------------
    if predict_file is not None:
        st.subheader("📁 Prediction on New Dataset")

        dataset1 = pd.read_csv(predict_file)
        d2 = dataset1.copy()

        dataset1 = pd.get_dummies(d2.iloc[:, [2, 3]], drop_first=True)
        M = sc.transform(dataset1)

        d2["y_pred"] = classifier.predict(M)

        st.dataframe(d2.head())

        csv = d2.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇ Download Predictions CSV",
            csv,
            "final1_prediction.csv",
            "text/csv"
        )

else:
    st.info("⬅ Upload training CSV to start")
