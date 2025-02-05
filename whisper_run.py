import streamlit as st
import whisper
from io import BytesIO
import gtts
from slang_dict import translation_dict_z_to_f, translation_dict_f_to_z, translation_dict_u_to_e
import re

# Load Whisper model
model = whisper.load_model("base")

# Function to transcribe audio using Whisper
def transcribe_audio_whisper(audio_file):
    result = model.transcribe(audio_file)
    return result['text']

# Function to convert text to speech
def speak_text(text):
    tts = gtts.gTTS(text)
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes

# Function to translate Gen Z slang to formal language
def translate_gen_z_to_formal(text):
    words = text.split()  # Split the input text into words
    translated_words = []
    for word in words:
        # Look up slang word in the dictionary, default to original word
        translated_word = translation_dict_z_to_f.get(word.lower(), word)
        # Preserve the original casing of the word
        if word.istitle():
            translated_word = translated_word.capitalize()
        translated_words.append(translated_word)
    return ' '.join(translated_words)

# Function to translate formal language to Gen Z slang
def translate_formal_to_gen_z(text):
    words = text.split()  # Split the input text into words
    translated_words = []
    for word in words:
        # Look up formal word in the dictionary, default to original word
        translated_word = translation_dict_f_to_z.get(word.lower(), word)
        # Preserve the original casing of the word
        if word.istitle():
            translated_word = translated_word.capitalize()
        translated_words.append(translated_word)
    return ' '.join(translated_words)

 # Function to translate urdu slang to formal language
def translate_urdu_to_formal(text):
    words = text.split()  # Split the input text into words
    translated_words = []
    for word in words:
        # Look up slang word in the dictionary, default to original word
        translated_word = translation_dict_u_to_e.get(word.lower(), word)
        # Preserve the original casing of the word
        if word.istitle():
            translated_word = translated_word.capitalize()
        translated_words.append(translated_word)
    return ' '.join(translated_words)

# Helper function to clean up text for matching (remove non-alphabetic chars)
def clean_text(text):
    return re.sub(r'[^a-zA-Z\s]', '', text).lower()

# Streamlit custom styling for UI
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(45deg, #6a11cb, #2575fc);
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #ff6f61;
            color: white;
            border-radius: 10px;
            font-weight: bold;
            width: 200px;
            height: 50px;
            transition: 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #ff4a35;
            transform: scale(1.05);
        }
        .stSelectbox>div {
            background-color: #ff6f61;
            color: white;
            border-radius: 8px;
        }
        .stTextInput>div {
            background-color: #ff6f61;
            border-radius: 10px;
        }
        .stTextInput>input {
            color: white;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
st.title("🎙️ Translator")
st.write("Talk and watch your speech transform! 🚀")

# Upload Audio File
audio_file = st.file_uploader("Upload an audio file 📂", type=["mp3", "wav", "m4a"])

if audio_file:
    # Save the uploaded file temporarily
    with open("temp_audio.mp3", "wb") as f:
        f.write(audio_file.read())
    
    # Transcribe with Whisper
    transcribed_text = transcribe_audio_whisper("temp_audio.mp3")

    if transcribed_text:
        # Clean up transcribed text for accurate translation
        cleaned_text = clean_text(transcribed_text)
        st.subheader("🎤 Transcribed Text:")
        st.write(transcribed_text)

        # Select Mode
        mode = st.selectbox("Choose Translation Mode 👇", ["Gen Z Slang", "Formal", "Urdu slang"])

        # Convert Text
        if mode == "Gen Z Slang":
            translated_text = translate_formal_to_gen_z(cleaned_text)
        elif mode == "Formal":
            translated_text = translate_gen_z_to_formal(cleaned_text)
        elif mode == "Urdu slang":
            translated_text = translate_urdu_to_formal(cleaned_text)    
        else:
            translated_text = None

        if translated_text:
            # Display Results
            st.subheader(f"🌀 Translated to {mode}:")
            st.write(translated_text)

            # Play TTS Output
            st.subheader("🔊 Hear the Translated Speech")
            audio_bytes = speak_text(translated_text)
            if audio_bytes:
                st.audio(audio_bytes, format="audio/mp3")

# New text input box for manual translation
st.subheader("🔠 Translate Your Own Sentence 📝")
input_text = st.text_input("Enter a sentence to translate:")

# Translation mode
if input_text:
    mode = st.selectbox("Choose Translation Mode 🕹️", ["Gen Z Slang", "Formal","Urdu Slang"], key="manual_mode")

    if mode == "Gen Z Slang":
        translated_input_text = translate_formal_to_gen_z(input_text)
    elif mode == "Formal":
        translated_input_text = translate_gen_z_to_formal(input_text)
    elif mode == "Urdu Slang":
        translated_input_text = translate_urdu_to_formal(input_text)
    else:
        translated_input_text = None

    st.subheader(f"🌀 Translated to {mode}:")
    st.write(translated_input_text)

    # Play TTS Output for Manual Input
    st.subheader("🔊 Hear the Translated Speech")
    audio_bytes = speak_text(translated_input_text)
    if audio_bytes:
        st.audio(audio_bytes, format="audio/mp3")
