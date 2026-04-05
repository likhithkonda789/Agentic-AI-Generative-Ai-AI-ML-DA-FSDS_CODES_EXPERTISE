import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

st.title("📊 CSV Full Information + Graphs")

file = st.file_uploader("Upload CSV file", type=["csv"])

if file is not None:

    # Load CSV
    df = pd.read_csv(file)
    st.success("File loaded successfully!")

    # ---------------- RAW DATA ----------------
    st.header("📄 Raw Data")
    st.dataframe(df)

    # ---------------- DATASET INFO ----------------
    st.header("ℹ️ Dataset Information")
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    st.text(info_str)

    # ---------------- SUMMARY STATS ----------------
    st.header("📊 Summary Statistics")
    st.write(df.describe(include="all"))

    # ---------------- MISSING VALUES ----------------
    st.header("❗ Missing Values")
    st.write(df.isnull().sum())

    # ---------------- VISUALIZATIONS ----------------
    st.header("📈 Graphs / Visualizations")

    columns = df.columns.tolist()
    graph_type = st.selectbox("Select graph type", 
                              ["Line Chart", "Bar Chart", "Histogram", "Pie Chart"])

    col = st.selectbox("Select column", columns)

    # === LINE CHART ===
    if graph_type == "Line Chart":
        try:
            st.line_chart(df[col])
        except:
            st.error("Line chart needs numeric values.")

    # === BAR CHART ===
    if graph_type == "Bar Chart":
        try:
            # If numeric → bar chart directly
            if pd.api.types.is_numeric_dtype(df[col]):
                st.bar_chart(df[col])
            else:
                # Categorical → value counts bar graph
                fig, ax = plt.subplots()
                df[col].value_counts().plot(kind='bar', ax=ax)
                st.pyplot(fig)
        except:
            st.error("Cannot generate bar chart for this column.")

    # === HISTOGRAM ===
    if graph_type == "Histogram":
        try:
            fig, ax = plt.subplots()
            df[col].dropna().hist(ax=ax, bins=30)
            ax.set_title(f"Histogram of {col}")
            st.pyplot(fig)
        except:
            st.error("Histogram requires numeric data.")

    # === PIE CHART ===
    if graph_type == "Pie Chart":
        try:
            fig, ax = plt.subplots()
            df[col].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
            ax.set_ylabel("")
            st.pyplot(fig)
        except:
            st.error("Pie chart requires categorical values.")

else:
    st.info("Upload a CSV file to continue.")
