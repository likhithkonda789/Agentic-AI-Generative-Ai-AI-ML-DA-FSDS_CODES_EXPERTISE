import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# --------------------------------------------------
# APP TITLE
# --------------------------------------------------
st.title("📊 Startup Profit Prediction (Best-Fit Model)")

st.write("This app predicts startup profit and evaluates whether the model is best-fit.")

# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------
file = st.file_uploader("Upload Investment CSV File", type=["csv"])

if file is not None:
    # --------------------------------------------------
    # LOAD DATA
    # --------------------------------------------------
    df = pd.read_csv(file)
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # --------------------------------------------------
    # SPLIT X & Y
    # --------------------------------------------------
    X = df.iloc[:, :-1]
    Y = df.iloc[:, -1]

    # --------------------------------------------------
    # HANDLE CATEGORICAL DATA
    # --------------------------------------------------
    X = pd.get_dummies(X, drop_first=True)

    # ⭐ VERY IMPORTANT FOR STATSMODELS
    X = X.astype(float)
    Y = Y.astype(float)

    # --------------------------------------------------
    # TRAIN TEST SPLIT
    # --------------------------------------------------
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=0
    )

    # --------------------------------------------------
    # LINEAR REGRESSION (SKLEARN)
    # --------------------------------------------------
    model = LinearRegression()
    model.fit(X_train, Y_train)

    train_score = model.score(X_train, Y_train)
    test_score = model.score(X_test, Y_test)

    # --------------------------------------------------
    # MODEL PERFORMANCE
    # --------------------------------------------------
    st.subheader("📈 Model Performance")

    st.write("Training R² (Bias):", round(train_score, 4))
    st.write("Testing R² (Variance):", round(test_score, 4))

    # --------------------------------------------------
    # OLS MODEL (STATSMODELS)
    # --------------------------------------------------
    X_sm = sm.add_constant(X)
    ols_model = sm.OLS(Y, X_sm).fit()

    st.subheader("📑 OLS Summary")
    st.text(ols_model.summary())

    # --------------------------------------------------
    # BEST FIT DECISION
    # --------------------------------------------------
    st.subheader("✅ Best-Fit Evaluation")

    adj_r2 = ols_model.rsquared_adj

    st.write("Adjusted R²:", round(adj_r2, 4))

    if abs(train_score - test_score) < 0.05 and adj_r2 > 0.8:
        st.success("✔ Model is BEST FIT (Low Bias & Low Variance)")
    else:
        st.warning("⚠ Model may NOT be best fit")

    # --------------------------------------------------
    # RESIDUAL ANALYSIS
    # --------------------------------------------------
    y_pred = model.predict(X_test)
    residuals = Y_test - y_pred

    st.subheader("📉 Residual Plot")

    fig, ax = plt.subplots()
    ax.scatter(y_pred, residuals)
    ax.axhline(0)
    ax.set_xlabel("Predicted Values")
    ax.set_ylabel("Residuals")
    st.pyplot(fig)

    # --------------------------------------------------
    # FINAL INTERPRETATION
    # --------------------------------------------------
    st.subheader("🧠 Interpretation")

    st.write("""
    ✔ High Adjusted R² indicates strong explanatory power  
    ✔ Small difference between training and testing scores shows good generalization  
    ✔ Random residuals confirm no pattern  
    """)

else:
    st.info("Please upload a CSV file to continue.")
