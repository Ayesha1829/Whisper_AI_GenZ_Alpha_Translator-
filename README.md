Gen Z & Gen Alpha Translator

📌 Project Overview

This project uses Whisper AI to transcribe speech and then translates it into Gen Z or Gen Alpha slang (and vice versa). The final output can also be played as speech using a Text-to-Speech (TTS) engine. 🎤🔥

🚀 Features

Speech-to-Text: Uses OpenAI Whisper to transcribe spoken words.

Slang Translator: Converts formal language to Gen Z/Alpha slang and vice versa.

Text-to-Speech (TTS): Reads out the translated text in an expressive voice.

Fun & Engaging: Ideal for entertainment, social media, and learning new slang!

🛠️ Tech Stack

Python (for processing and AI integration)

OpenAI Whisper (for speech-to-text transcription)

NLP (Natural Language Processing) (for slang translation)

Google TTS / ElevenLabs (for speech output)

Next.js (Optional) (if a web interface is added)

📂 Project Structure

📦 gen-z-translator
 ┣ 📂 src
 ┃ ┣ 📜 whisper_transcriber.py  # Handles speech-to-text conversion
 ┃ ┣ 📜 slang_converter.py       # Converts text into Gen Z/Alpha slang
 ┃ ┣ 📜 tts_generator.py        # Converts text back into speech
 ┣ 📜 app.py                     # Main script
 ┣ 📜 requirements.txt           # Dependencies
 ┣ 📜 README.md                  # This file

🔧 Installation & Setup

Clone this repository:

git clone https://github.com/your-username/gen-z-translator.git
cd gen-z-translator

Install dependencies:

pip install -r requirements.txt

Run the project:

python app.py

🗣️ Usage

Run the script and input an audio file.

Choose translation mode (Normal → Gen Z or Gen Z → Normal).

Listen to the output speech or read the transcription!

🔥 Future Enhancements

Add more slang translations dynamically.

Support more languages.

Create a web-based UI for accessibility.

