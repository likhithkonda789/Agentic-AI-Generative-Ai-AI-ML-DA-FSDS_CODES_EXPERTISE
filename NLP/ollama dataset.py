import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ollama
import os

# -----------------------------
# AI Insights (SAFE FOR SMALL MODEL)
# -----------------------------
def generate_ai_insights(df_summary):
    try:
        prompt = (
            "You are a data analyst. "
            "Give 5 short and simple insights from this dataset summary:\n\n"
            f"{df_summary}"
        )

        response = ollama.chat(
            model='gemma3:270 ',   # EXACT model name
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"AI Insights Error: {str(e)}"

# -----------------------------
# Generate Visualizations
# -----------------------------
def generate_visualizations(df):
    plot_paths = []

    # Histograms for numeric columns
    for col in df.select_dtypes(include=["number"]).columns:
        plt.figure(figsize=(5, 3))
        sns.histplot(df[col], bins=20, kde=True)
        plt.title(f"{col} Distribution")
        path = f"{col}_hist.png"
        plt.savefig(path)
        plt.close()
        plot_paths.append(path)

    # Correlation heatmap
    if not df.select_dtypes(include=["number"]).empty:
        plt.figure(figsize=(6, 4))
        sns.heatmap(df.corr(numeric_only=True), cmap="coolwarm", annot=False)
        path = "correlation_heatmap.png"
        plt.savefig(path)
        plt.close()
        plot_paths.append(path)

    return plot_paths

# -----------------------------
# Main EDA Function
# -----------------------------
def eda_analysis(file_path):
    try:
        df = pd.read_csv(file_path)

        # Handle missing values
        for col in df.select_dtypes(include="number"):
            df[col] = df[col].fillna(df[col].median())

        for col in df.select_dtypes(include="object"):
            df[col] = df[col].fillna(df[col].mode()[0])

        summary = df.describe().to_string()
        missing = df.isnull().sum().to_string()

        insights = generate_ai_insights(summary)
        plots = generate_visualizations(df)

        report = f"""
DATA LOADED SUCCESSFULLY ✅

SUMMARY:
{summary}

MISSING VALUES:
{missing}

AI INSIGHTS:
{insights}
"""

        return report, plots

    except Exception as e:
        return f"EDA Error: {str(e)}", []

# -----------------------------
# Gradio Interface
# -----------------------------
demo = gr.Interface(
    fn=eda_analysis,
    inputs=gr.File(type="filepath", label="Upload CSV File"),
    outputs=[
        gr.Textbox(label="EDA Report"),
        gr.Gallery(label="Visualizations")
    ],
    title="📊 AI-Powered Exploratory Data Analysis",
    description="Upload a CSV file to get automated EDA, charts, and AI insights."
)

# -----------------------------
# Launch App
# -----------------------------
demo.launch(share=True)
