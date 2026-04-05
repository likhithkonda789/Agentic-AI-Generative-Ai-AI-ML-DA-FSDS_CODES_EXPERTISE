from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from langchain.chat_models import ChatOpenAI

import streamlit as st
import os
#from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = "AIzaSyBmHhSrU2YzPMJJNTTwC896xiwF49yDuT4"
#os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"

os.environ["LANGCHAIN_API_KEY"]= "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"
#os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","I am chatbot. I am hear to assist you. Please type your queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('LLM-OPENAI PROJECT - CUSTOM GPT-5 BY likhith')
input_text=st.text_input("How may I help you")

# openAI LLm
llm=ChatOpenAI(model="gpt-4.1", temperature=0.2)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
    