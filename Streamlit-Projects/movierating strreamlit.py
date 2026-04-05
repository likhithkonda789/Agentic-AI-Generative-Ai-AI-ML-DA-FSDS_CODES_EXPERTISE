import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="Movie Ratings Dashboard", layout="wide")
st.title("🎬 Movie Ratings Full Information App (Fixed)")

# ----------- File Upload (or load default file if present) -----------
uploaded_file = st.file_uploader("Upload Movie-Rating.csv", type=["csv"])

if uploaded_file is None:
    # try loading default provided file path (useful if you're running this where file exists)
    try:
        df = pd.read_csv("/mnt/data/Movie-Rating.csv")
        st.info("Loaded default file at /mnt/data/Movie-Rating.csv")
    except Exception:
        df = None
else:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error reading uploaded CSV: {e}")
        df = None

if df is None:
    st.warning("No dataset available. Please upload Movie-Rating.csv (or place it at /mnt/data/Movie-Rating.csv).")
else:
    st.success("CSV Loaded Successfully!")

    # ----------- Show Raw Data -----------
    st.header("📄 Dataset Preview")
    st.dataframe(df)

    # ----------- Dataset Info (fixed) -----------
    st.header("📊 Dataset Information (types & non-null counts)")

    try:
        buf = io.StringIO()
        df.info(buf=buf)             # capture info into buffer
        info_str = buf.getvalue()
        st.text(info_str)            # show captured info
    except Exception as e:
        st.error("Failed to get df.info() output:")
        st.exception(e)

    # show dtypes and shape too (redundant but helpful)
    st.write("**Shape:**", df.shape)
    st.write("**Column dtypes:**")
    st.table(pd.DataFrame(df.dtypes, columns=["dtype"]))

    # ----------- Summary Stats -----------
    st.header("📈 Summary Statistics")
    try:
        st.dataframe(df.describe(include="all").T)
    except Exception as e:
        st.error("Could not compute describe():")
        st.exception(e)

    # ----------- Filters -----------
    st.header("🔎 Filter Movies")
    if "Genre" in df.columns:
        genres = ["All"] + sorted(df["Genre"].dropna().unique().tolist())
        selected_genre = st.selectbox("Select Genre", genres)
        if selected_genre != "All":
            filtered_df = df[df["Genre"] == selected_genre]
        else:
            filtered_df = df.copy()
    else:
        st.info("No 'Genre' column found — showing full dataset.")
        filtered_df = df.copy()

    st.subheader(f"Filtered Results ({len(filtered_df)} movies)")
    st.dataframe(filtered_df)

    # ----------- Charts -----------
    st.header("📉 Visualizations")

    # Rotten Tomatoes vs Audience Ratings
    if {"Rotten Tomatoes Ratings %", "Audience Ratings %"}.issubset(df.columns):
        st.subheader("Rotten Tomatoes vs Audience Ratings")
        fig1, ax1 = plt.subplots(figsize=(6,4))
        ax1.scatter(filtered_df["Rotten Tomatoes Ratings %"], filtered_df["Audience Ratings %"])
        ax1.set_xlabel("Rotten Tomatoes Rating %")
        ax1.set_ylabel("Audience Rating %")
        ax1.set_title("Ratings Comparison")
        plt.tight_layout()
        st.pyplot(fig1)
    else:
        st.info("Columns for Ratings comparison not found.")

    # Budget by Year
    if {"Budget (million $)", "Year of release"}.issubset(df.columns):
        st.subheader("Average Budget by Year of Release")
        try:
            yearly_budget = filtered_df.groupby("Year of release")["Budget (million $)"].mean().sort_index()
            fig2, ax2 = plt.subplots(figsize=(8,4))
            yearly_budget.plot(kind="bar", ax=ax2)
            ax2.set_xlabel("Year")
            ax2.set_ylabel("Avg Budget (Million $)")
            ax2.set_title("Average Movie Budget per Year")
            plt.tight_layout()
            st.pyplot(fig2)
        except Exception as e:
            st.error("Failed to plot budget by year:")
            st.exception(e)
    else:
        st.info("Columns for Budget/Year chart not found.")

    # ----------- Download Button -----------
    st.header("⬇️ Download Filtered Data")
    try:
        csv_data = filtered_df.to_csv(index=False)
        st.download_button("Download CSV", csv_data, "filtered_movies.csv", "text/csv")
    except Exception as e:
        st.error("Could not prepare download:")
        st.exception(e)
