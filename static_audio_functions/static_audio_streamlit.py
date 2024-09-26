# streamlit.py
import app as st
from static_audio import transcribe_audio, get_gpt_response, save_uploaded_file
import os

# Streamlit app setup
st.title("Audio to Text with GPT-4")

st.write("Click the button below to upload an audio file and get a response from GPT-4.")

# Upload audio file
audio_file = st.file_uploader("Upload Audio", type=["mp3", "wav", "m4a", "ogg"])

if audio_file is not None:
    st.audio(audio_file, format=audio_file.type)
    
    # Save the uploaded file to a temporary location
    file_path = save_uploaded_file(audio_file)

    with st.spinner("Transcribing audio..."):
        transcript = transcribe_audio(file_path)  # Pass the file path to the transcribe_audio function
        st.write("Transcription:", transcript)

        st.write("Generating response from GPT-4...")
        response = get_gpt_response(transcript)
        st.write("GPT-4 Response:", response)

    # Clean up: Remove the temporary file after processing
    if os.path.exists(file_path):
        os.remove(file_path)