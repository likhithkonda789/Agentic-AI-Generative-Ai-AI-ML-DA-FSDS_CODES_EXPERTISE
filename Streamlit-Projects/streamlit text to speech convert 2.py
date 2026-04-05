import streamlit as st
import asyncio
import edge_tts

st.title("🎤 Text to Speech App (Male & Female Voices)")

text = st.text_area("Enter your text here:")

# Voice options (male + female for multiple languages)
voices = {
    "English - Female": "en-US-AnaNeural",
    "English - Male": "en-US-GuyNeural",
    "Hindi - Female": "hi-IN-SwaraNeural",
    "Hindi - Male": "hi-IN-MadhurNeural",
    "Telugu - Female": "te-IN-ShrutiNeural",
    "Telugu - Male": "te-IN-MohanNeural",
    "Kannada - Female": "kn-IN-SapnaNeural",
    "Kannada - Male": "kn-IN-GaganNeural",
    "Marathi - Female": "mr-IN-AarohiNeural",
    "Marathi - Male": "mr-IN-MadhurNeural"
}

voice_name = st.selectbox("Select Voice (Language + Male/Female)", list(voices.keys()))
selected_voice = voices[voice_name]

async def generate_voice():
    communicate = edge_tts.Communicate(text, selected_voice)
    await communicate.save("speech.mp3")

if st.button("Convert to Speech"):
    if text.strip() == "":
        st.warning("Please enter some text!")
    else:
        asyncio.run(generate_voice())
        audio_file = open("speech.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")
        st.success("Audio generated successfully! 🎧")
