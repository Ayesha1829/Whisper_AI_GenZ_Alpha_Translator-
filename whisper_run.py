import streamlit as st
import whisper
import openai
import gtts
import os
from io import BytesIO

# Set OpenAI API Key (DO NOT expose in code)
openai.api_key = "your api key"
# Load Whisper Model (Base for speed)
model = whisper.load_model("base")

# Define Gen Z & Gen Alpha Translator function using the new OpenAI API
# Define Gen Z & Gen Alpha Translator function
def translate_text(text, mode):
    prompt = f"Convert this sentence into {mode} style: {text}"
    response = openai.completions.create(
        model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" for free-tier users
        prompt=prompt,
        max_tokens=200  # Adjust token limit as per your needs
    )
    return response['choices'][0]['text'].strip()


# Text-to-Speech Function
def speak_text(text):
    tts = gtts.gTTS(text)
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes

# Streamlit UI
st.title("🎙️ Gen Z & Gen Alpha Translator")
st.write("Talk and watch your speech transform! 🚀")

# Upload Audio File
audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if audio_file:
    # Save uploaded file
    audio_path = "temp_audio.mp3"
    with open(audio_path, "wb") as f:
        f.write(audio_file.read())

    # Transcribe using Whisper
    result = model.transcribe(audio_path)
    transcribed_text = result["text"]

    # Select Mode
    mode = st.selectbox("Choose Translation Mode", ["Gen Z Slang", "Gen Alpha Formal"])

    # Convert Text
    translated_text = translate_text(transcribed_text, mode)

    # Display Results
    st.subheader("🎤 Transcribed Text:")
    st.write(transcribed_text)

    st.subheader(f"🌀 Translated to {mode}:")
    st.write(translated_text)

    # Play TTS Output
    st.subheader("🔊 Hear the Translated Speech")
    audio_bytes = speak_text(translated_text)
    st.audio(audio_bytes, format="audio/mp3")

    # Cleanup after processing
    os.remove(audio_path)
