# streamlit.py
import app as st
from fixed_time import record_audio, transcribe_audio, get_gpt_response
import os

st.title("Microphone to Text Transcription with Whisper & GPT-4")

# Set recording parameters
duration = st.slider("Select Recording Duration (seconds)", 1, 10, 5)
fs = 16000  # Sample rate (Hz)

if st.button("Start Recording"):
    temp_audio_file = "temp_audio.wav"  # Temporary file to save the recorded audio
    record_audio(duration, fs, temp_audio_file)
    
    with st.spinner("Transcribing..."):
        transcription = transcribe_audio(temp_audio_file)
        st.write("Transcription:", transcription)

        if "Error" not in transcription:
            # Send transcription to GPT-4 for a response
            st.write("Generating response from GPT-4...")
            gpt_response = get_gpt_response(transcription)
            st.write("GPT-4 Response:", gpt_response)

    # Clean up: Remove the temporary audio file after processing
    if os.path.exists(temp_audio_file):
        os.remove(temp_audio_file)
