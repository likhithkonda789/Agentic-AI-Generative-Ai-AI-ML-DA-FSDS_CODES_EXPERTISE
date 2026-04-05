import streamlit as st
from gtts import gTTS
import os

st.set_page_config(page_title="Text to Speech App")

st.title("🔊 Text to Speech App")
st.write("Type your text and convert it into voice")

text = st.text_area("Enter your text here:")

language = st.selectbox("Select Language", ["en", "hi","te","kn", "mr"])

if st.button("Convert to Speech"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        tts = gTTS(text=text, lang=language)
        tts.save("speech.mp3")

        audio_file = open("speech.mp3", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")
        st.success("✅ Audio Generated Successfully!")
