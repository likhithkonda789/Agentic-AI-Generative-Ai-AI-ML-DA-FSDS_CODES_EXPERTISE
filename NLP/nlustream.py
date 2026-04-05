import streamlit as st
from gtts import gTTS
import os
from langdetect import detect, lang_detect_exception
from googletrans import Translator
import pycountry
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
import nltk

# Download NLTK data
nltk.download('punkt')
nltk.download('words')

# Function to read text aloud
def read_aloud(text, language='en'):
    tts = gTTS(text=text, lang=language)
    tts.save("temp.mp3")
    os.system("start temp.mp3")

# Function to generate word cloud
def generate_wordcloud(text):
    english_words = set(nltk.corpus.words.words())
    words = word_tokenize(text)
    english_words_in_text = [word for word in words if word.lower() in english_words]
    english_text = ' '.join(english_words_in_text)
    
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(english_text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    plt.tight_layout()
    return fig

# Main Streamlit app
st.title("Globalize")

# Set background image using custom CSS
background_image = "back.jpg"  # Replace with your background image file name
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:streamlit_env\back.jpg;base64,{background_image});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Create a two-column layout
col1, col2 = st.columns(2)

# Get user input
with col1:
    paragraph = st.text_area("Enter one paragraph:")

with col2:
    # Get list of all languages
    all_languages = [lang.name for lang in pycountry.languages]

    # Get user input for target languages
    target_languages_input = st.multiselect("Select the desired languages for translation:", all_languages)

# Button to read aloud
if st.button("Read Aloud"):
    read_aloud(paragraph)

# Detect the language of the input paragraph
paragraph_language = None  # Initialize paragraph_language outside the try block
if paragraph.strip():  # Check if paragraph is not empty
    try:
        paragraph_language = detect(paragraph)
        language_name = pycountry.languages.get(alpha_2=paragraph_language).name
        st.write("Detected language:", language_name)
    except lang_detect_exception.LangDetectException as e:
        st.error("Language detection failed: {}".format(e))
        paragraph_language = 'en'
        language_name = 'English'
    except KeyError:
        st.error("Language code not found in pycountry")
        language_name = 'Unknown'
    except Exception as e:
        st.error("Error occurred during language detection: {}".format(e))

# Translate the paragraph to English if it's not already in English
translator = Translator()
if paragraph_language and paragraph_language != 'en':
    translated_paragraph = translator.translate(paragraph, dest='en').text
    st.write("Translated to universal language English:", translated_paragraph)
else:
    translated_paragraph = paragraph

# Generate and display word cloud
if translated_paragraph.strip():  # Check if translated paragraph is not empty
    try:
        # Encode text to UTF-8 to handle non-Unicode characters
        translated_paragraph = translated_paragraph.encode('utf-8', 'ignore').decode('utf-8')
        wordcloud_fig = generate_wordcloud(translated_paragraph)
        st.sidebar.subheader("Word Cloud")
        st.sidebar.pyplot(wordcloud_fig)
    except Exception as e:
        st.error(f"Error generating word cloud: {e}")

# Add image below the word cloud
st.sidebar.subheader("Image")
#st.sidebar.image("languages.jpg", use_column_width=True)

# Translate and read aloud
if st.button("Translate and Read Aloud"):
    target_languages = []
    for lang_name in target_languages_input:
        lang_code = pycountry.languages.lookup(lang_name).alpha_2
        target_languages.append(lang_code)
    
    # Translate the paragraph into each target language, print, and read aloud
    for target_language in target_languages:
        try:
            translated_paragraph = translator.translate(paragraph, dest=target_language).text
            language_name = pycountry.languages.get(alpha_2=target_language).name
            st.write(f"\nTranslated paragraph in {language_name}:")
            st.write(translated_paragraph)
            
            # Read translated text aloud
            read_aloud(translated_paragraph, target_language)
        except Exception as e:
            st.error(f"Translation to {language_name} failed: {e}")
