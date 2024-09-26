# Microphone to Text Transcription with GPT-4 Integration

This project is an AI-powered transcription system that converts audio recordings into text using OpenAI's Whisper model and generates intelligent responses using GPT-4. The app is built with Streamlit for a simple and responsive UI, allowing users to record audio, transcribe it, and get responses in real-time.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Workflow](#workflow)
- [How to Set Up the Project](#how-to-set-up-the-project)
- [How to Run the Project](#how-to-run-the-project)
- [Folders Explanation](#folders-explanation)


## Features

- **Real-Time Audio Transcription:** Convert voice input from Microphone into accurate text using OpenAI's Whisper model.
- **AI-Powered Responses:** Leverage GPT-4 to generate intelligent responses from transcribed audio.
- **Streamlit Integration:** Simple and user-friendly web interface for recording, transcribing, and interacting with GPT-4.
- **Conversation Storage:** Transcriptions and AI responses are stored in JSON format for further analysis.

## Technologies Used

- **OpenAI Whisper Model:** Used for accurate and fast audio-to-text conversion.
- **GPT-4:** Generates intelligent responses from transcribed audio.
- **Streamlit:** A web application framework used to create the interface for recording and viewing transcription results.
- **NumPy:** Handles numerical operations required during audio processing.
- **SoundDevice & SoundFile:** Libraries used for recording audio from the microphone and saving it in standard audio formats.

## Project Structure

├── app.py                           # Streamlit UI and app logic
├── main.py                          # Contains audio recording, transcription, and GPT-4 response logic
├── input_audio/                     # Folder to store recorded audio files
├── transcribe_output/               # Folder to store transcription and response in JSON format
├── requirements.txt                 # Python dependencies
└── README.md                        # This README file

## How to Set Up the Project
Clone the repository:

bash
git clone https://github.com/your-username/microphone-to-text-gpt4.git

- Navigate to the project directory:

bash
cd microphone-to-text-gpt4

- Install the dependencies:

bash
pip install -r requirements.txt

- Set up environment variables:

## Create a .env file in the root directory and add your OpenAI API key:

- makefile
- Copy code
- OPENAI_API_KEY=your_openai_api_key_here
- How to Run the Project

## Start the Streamlit app:

bash
streamlit run app.py


## Folders Explanation

### static_audio_functions
This folder has two files: one for the Streamlit interface and the other for the main code. Its main purpose is to allow users to upload an audio file from their local machine, which gets transcribed, and then the user receives an LLM response.

### fixed_time_functions
This folder also has two files: one for the Streamlit interface and the other for the main file, which includes the fixed time limit function. You can start a conversation by selecting a fixed time range for voice input (e.g., 10 seconds) from the UI. After clicking "Start Conversation," the Whisper model will listen for the specified duration and then provide the text transcript on the screen along with an AI response.




🚀 Excited to showcase my latest project: Audio Transcription with Whisper! 🚀

In this project, I utilized OpenAI's Whisper model to build a powerful audio transcription system that efficiently converts spoken words into text. 🎯

🔑 Key Features:

Whisper Model Integration for accurate speech-to-text transcription 📚
Real-time Transcription for seamless and quick conversion of audio to text in a user-friendly interface 🗣️
Language Detection and handling of various audio file formats 🔄
Error Handling for smoother user experience, ensuring robust performance even with noisy inputs 💬
💻 Working Flow:

Users upload an audio file through the interface.
The Whisper model processes the audio to transcribe speech into text.
The transcribed text is displayed for users to review, edit, or download.
Additional metadata such as timestamps and language detection is optionally included in the output.
🔧 Technologies:

Whisper by OpenAI: A state-of-the-art speech-to-text model that handles multiple languages and various audio qualities.
Python: Used for building the logic and integrating the Whisper model.
Streamlit: A simple yet powerful framework to create an interactive, user-friendly web interface for audio uploads and displaying transcriptions.
Pydub: A Python library used for handling audio files, converting them into formats suitable for transcription.
🛠️ How to Run the Project:

Clone the repository and navigate to the project folder.
Install the necessary dependencies:
pip install -r requirements.txt
Run the Streamlit app to upload audio files and start the transcription:
streamlit run app.py
💡 Want to explore the project? Feel free to check out the GitHub repository here 👉 [Insert GitHub Repo Link]

#GeeksVisor #TeamGeeksVisor #AI #Whisper #AudioTranscription #OpenAI #SpeechToText #Python #Streamlit