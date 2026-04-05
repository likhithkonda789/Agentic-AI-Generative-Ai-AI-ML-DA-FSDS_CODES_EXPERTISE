import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

st.set_page_config(page_title="Iris Dataset Explorer", layout="wide")

st.title("🌸 Iris Dataset – Full Information App")

# File uploader
file = st.file_uploader("Upload Iris.csv file", type=["csv"])

if file is not None:

    # Read CSV
    df = pd.read_csv(file)
    st.success("CSV Loaded Successfully!")

    # -------------------------------- RAW DATA --------------------------------
    st.header("📄 Raw Data")
    st.dataframe(df)

    # -------------------------------- DATASET INFO --------------------------------
    st.header("ℹ️ Dataset Information (df.info())")
    buffer = io.StringIO()
    df.info(buf=buffer)
    info = buffer.getvalue()
    st.text(info)

    # -------------------------------- SUMMARY STATISTICS --------------------------------
    st.header("📊 Summary Statistics")
    st.write(df.describe(include="all"))

    # -------------------------------- MISSING VALUES --------------------------------
    st.header("❗ Missing Values")
    st.write(df.isnull().sum())

    # -------------------------------- VISUALIZATIONS --------------------------------
    st.header("📈 Visualizations")

    graph_type = st.selectbox(
        "Select Graph Type",
        ["Line Chart", "Bar Chart", "Histogram", "Pie Chart", "Correlation Heatmap"]
    )

    columns = df.columns.tolist()
    
    # For graphs that need a column
    col = None
    if graph_type != "Correlation Heatmap":
        col = st.selectbox("Select Column", columns)

    # === LINE CHART ===
    if graph_type == "Line Chart":
        try:
            st.line_chart(df[col])
        except:
            st.error("Line chart needs numeric values.")

    # === BAR CHART ===
    if graph_type == "Bar Chart":
        try:
            if df[col].dtype in ['float64', 'int64']:
                st.bar_chart(df[col])
            else:
                fig, ax = plt.subplots()
                df[col].value_counts().plot(kind="bar", ax=ax)
                st.pyplot(fig)
        except:
            st.error("Unable to plot bar chart.")

    # === HISTOGRAM ===
    if graph_type == "Histogram":
        try:
            fig, ax = plt.subplots()
            df[col].dropna().hist(ax=ax, bins=25)
            st.pyplot(fig)
        except:
            st.error("Histogram requires numeric values.")

    # === PIE CHART ===
    if graph_type == "Pie Chart":
        try:
            fig, ax = plt.subplots()
            df[col].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
            ax.set_ylabel("")
            st.pyplot(fig)
        except:
            st.error("Pie chart requires categorical values.")

    # === CORRELATION HEATMAP ===
    if graph_type == "Correlation Heatmap":
        fig, ax = plt.subplots(figsize=(6,4))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
        st.pyplot(fig)

    # -------------------------------- FILTERING DATA --------------------------------
    st.header("🔍 Filter Data")
    filter_col = st.selectbox("Select Column to Filter", df.columns)

    unique_vals = df[filter_col].unique()
    selected_vals = st.multiselect("Select Value(s)", unique_vals)

    if selected_vals:
        filtered_df = df[df[filter_col].isin(selected_vals)]
    else:
        filtered_df = df

    st.subheader("Filtered Data")
    st.dataframe(filtered_df)

    # -------------------------------- DOWNLOAD --------------------------------
    st.header("⬇️ Download Processed Data")
    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", csv, "filtered_data.csv", "text/csv")

else:
    st.info("Please upload the Iris.csv file to continue.")
