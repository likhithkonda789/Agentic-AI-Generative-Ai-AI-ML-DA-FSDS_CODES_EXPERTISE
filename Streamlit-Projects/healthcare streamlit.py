import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App Title
st.title("📊 CSV File Explorer – Full Information Dashboard")

# Upload CSV File
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read File
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    # --- FILE INFO ---
    st.header("📄 File Information")
    st.write(f"**Rows:** {df.shape[0]}")
    st.write(f"**Columns:** {df.shape[1]}")

    # Show columns
    st.subheader("📌 Column Names")
    st.write(df.columns.tolist())

    # --- DATAFRAME PREVIEW ---
    st.header("🔍 Data Preview")
    st.dataframe(df)

    # --- SUMMARY STATISTICS ---
    st.header("📈 Summary Statistics")
    st.write(df.describe())

    # --- FILTER SECTION ---
    st.header("🧭 Filter Data")

    col = st.selectbox("Select a column to filter", df.columns)
    if df[col].dtype != 'object':
        min_val, max_val = float(df[col].min()), float(df[col].max())
        selected_range = st.slider("Select Value Range", min_val, max_val, (min_val, max_val))
        filtered_df = df[(df[col] >= selected_range[0]) & (df[col] <= selected_range[1])]
    else:
        unique_vals = df[col].unique()
        selected_val = st.selectbox("Select Value", unique_vals)
        filtered_df = df[df[col] == selected_val]

    st.write("Filtered Data:")
    st.dataframe(filtered_df)

    # --- PLOT SECTION ---
    st.header("📊 Visualization")

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if len(numeric_cols) >= 1:
        selected_plot_col = st.selectbox("Choose a numeric column to plot histogram", numeric_cols)

        fig, ax = plt.subplots()
        ax.hist(df[selected_plot_col])
        ax.set_title(f"Histogram of {selected_plot_col}")
        ax.set_xlabel(selected_plot_col)
        ax.set_ylabel("Frequency")

        st.pyplot(fig)
    else:
        st.info("No numeric columns available for plotting.")

else:
    st.warning("Please upload a CSV file to continue.")
