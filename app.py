# app.py
import streamlit as st
from main import record_audio, transcribe_audio, get_gpt_response
import os

st.title("Microphone to Text Transcription with Whisper & GPT-4")

# Set recording parameters
fs = 16000  # Sample rate (Hz)

if st.button("Start Conversation"):
    temp_audio_file = record_audio(fs)
    
    with st.spinner("Transcribing..."):
        transcription = transcribe_audio(temp_audio_file)
        st.write("Transcription:", transcription)

        if "Error" not in transcription:
            # Send transcription to GPT-4 for a response
            st.write("Generating response from GPT-4...")
            gpt_response = get_gpt_response(transcription)
            st.write("GPT-4 Response:", gpt_response)
