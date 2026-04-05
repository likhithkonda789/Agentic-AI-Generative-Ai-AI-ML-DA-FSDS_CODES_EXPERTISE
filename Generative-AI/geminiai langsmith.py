import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# ==============================
# 🔐 API KEYS & LANGSMITH SETUP
# ==============================
os.environ["GOOGLE_API_KEY"] = "AIzaSyDNdYAayZ76fJZdo_4umbP-VAcgxegcge4"
# Enable LangSmith tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"
# ==============================
# 🧠 Prompt Template
# ==============================
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are Gemini 2.5 Flash — a fast, multimodal, and intelligent AI assistant. Please respond clearly and helpfully."),
        ("user", "Question: {question}")
    ]
)
# ==============================
# ⚙️ Streamlit UI
# ==============================
st.title("🤖 GEMINI 2.5 FLASH CHATBOT - POWERED BY LANGSMITH ")
input_text = st.text_input("💬 Ask me anything:")
# ==============================
# 🌟 Gemini 2.5 Flash Model Setup
# ==============================
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",   # ✅ Correct model name
    temperature=0.2,
    max_output_tokens=1024
)
# Output parser for string responses
output_parser = StrOutputParser()
# Combine into LCEL chain
chain = prompt | llm | output_parser
# ==============================
# 💬 Handle User Input
# ==============================
if input_text:
    with st.spinner("🤔 Gemini 2.5 Flash is generating a response..."):
        try:
            response = chain.invoke({"question": input_text})
            st.success("✅ Here's my response:")
            st.write(response)
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")