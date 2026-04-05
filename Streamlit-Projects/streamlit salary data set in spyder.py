import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from scipy.stats import variation
import scipy.stats as stats

st.set_page_config(page_title="Salary Prediction - Simple Linear Regression", layout="wide")

st.title("💼 Salary Prediction using Simple Linear Regression")

# =========================
# Upload CSV
# =========================
uploaded_file = st.file_uploader("Upload Salary_Data.csv", type=["csv"])

if uploaded_file is not None:
    dataset = pd.read_csv(uploaded_file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(dataset)

    # =========================
    # Features & Target
    # =========================
    x = dataset.iloc[:, :-1]
    y = dataset.iloc[:, -1]

    # =========================
    # Train Test Split
    # =========================
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=0
    )

    # =========================
    # Model Training
    # =========================
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    y_pred = regressor.predict(x_test)

    # =========================
    # Prediction Comparison
    # =========================
    st.subheader("📊 Actual vs Predicted")
    comparison = pd.DataFrame({
        "Actual Salary": y_test.values,
        "Predicted Salary": y_pred
    })
    st.dataframe(comparison)

    # =========================
    # Visualization
    # =========================
    st.subheader("📈 Regression Graph")

    fig, ax = plt.subplots()
    ax.scatter(x_test, y_test)
    ax.plot(x_train, regressor.predict(x_train))
    ax.set_xlabel("Years of Experience")
    ax.set_ylabel("Salary")
    ax.set_title("Salary vs Experience")
    st.pyplot(fig)

    # =========================
    # Model Parameters
    # =========================
    st.subheader("📐 Model Parameters")

    c_inter = regressor.intercept_
    m_coef = regressor.coef_[0]

    st.write(f"**Intercept (c):** {c_inter}")
    st.write(f"**Coefficient (m):** {m_coef}")

    # =========================
    # Future Predictions
    # =========================
    st.subheader("🔮 Future Salary Prediction")

    exp_years = st.number_input("Enter Years of Experience", min_value=0.0, step=0.5)
    future_salary = m_coef * exp_years + c_inter
    st.success(f"Predicted Salary: ₹ {future_salary:.2f}")

    # =========================
    # Model Evaluation
    # =========================
    st.subheader("📉 Model Performance")

    bias_training = regressor.score(x_train, y_train)
    variance_testing = regressor.score(x_test, y_test)

    st.write(f"**Training Score (Bias):** {bias_training}")
    st.write(f"**Testing Score (Variance):** {variance_testing}")

    # =========================
    # Statistical Analysis
    # =========================
    st.subheader("📊 Statistical Analysis")

    stats_df = pd.DataFrame({
        "Mean": dataset.mean(),
        "Median": dataset.median(),
        "Variance": dataset.var(),
        "Std Deviation": dataset.std(),
        "Skewness": dataset.skew(),
        "SEM": dataset.sem()
    })

    st.dataframe(stats_df)

    # =========================
    # Coefficient of Variation
    # =========================
    st.subheader("📐 Coefficient of Variation")

    cv_df = pd.DataFrame({
        "CV": variation(dataset)
    }, index=dataset.columns)

    st.dataframe(cv_df)

    # =========================
    # Correlation
    # =========================
    st.subheader("🔗 Correlation Matrix")
    st.dataframe(dataset.corr())

    # =========================
    # Z-Score
    # =========================
    st.subheader("📏 Z-Score Normalization")
    zscore_df = dataset.apply(stats.zscore)
    st.dataframe(zscore_df)

    # =========================
    # ANOVA-like Calculations
    # =========================
    st.subheader("📘 ANOVA Metrics")

    y_mean = np.mean(y)
    SSR = np.sum((y_pred - y_mean) ** 2)

    y_small = y.iloc[:len(y_pred)]
    SSE = np.sum((y_small - y_pred) ** 2)

    mean_total = np.mean(dataset.values)
    SST = np.sum((dataset.values - mean_total) ** 2)

    r_square = 1 - (SSR / SST)

    st.write(f"**SSR:** {SSR}")
    st.write(f"**SSE:** {SSE}")
    st.write(f"**SST:** {SST}")
    st.write(f"**R² Score:** {r_square}")

else:
    st.info("👆 Upload Salary_Data.csv to start")
