# app.py
import openai
import sounddevice as sd
import app as st
import soundfile as sf
import os
from dotenv import load_dotenv
import numpy as np

# Load environment variables
load_dotenv()

# Set your OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Create directories if they do not exist
input_audio_dir = "input_audio"
transcribe_output_dir = "transcribe_output"
os.makedirs(input_audio_dir, exist_ok=True)
os.makedirs(transcribe_output_dir, exist_ok=True)

def record_audio(fs, device=1, threshold=0.01, pause_duration=2):
    """Record audio dynamically from the microphone until a pause is detected."""
    st.info("Recording... Press Ctrl+C to stop.")
    
    if device is None:
        device = sd.default.device[0]  # Use default microphone if device not specified
    
    recording_data = []
    sd.default.samplerate = fs
    sd.default.channels = 1

    def callback(indata, frames, time, status):
        """Callback function to capture audio in chunks and detect silence."""
        volume_norm = np.linalg.norm(indata) * 10
        recording_data.append(indata.copy())
        if volume_norm < threshold:  # Silence detection
            st.info(f"Detected silence... Waiting for {pause_duration} seconds.")
            sd.sleep(int(pause_duration * 1000))
            sd.CallbackAbort()

    # Record until 2 seconds of silence
    with sd.InputStream(callback=callback):
        sd.sleep(5000)  # Placeholder, use an appropriate time or manually stop

    # Save audio file to input_audio folder
    audio_file_path = os.path.join(input_audio_dir, "conversation_audio.wav")
    sf.write(audio_file_path, np.concatenate(recording_data), fs)
    st.success(f"Recording finished and saved at {audio_file_path}")
    
    return audio_file_path

def transcribe_audio(file_path):
    """Send audio to OpenAI Whisper for transcription."""
    try:
        with open(file_path, "rb") as audio_file:
            response = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        
        # Save transcription to transcribe_output folder
        transcription = response.text
        transcription_file_path = os.path.join(transcribe_output_dir, "conversation_transcript.txt")
        with open(transcription_file_path, "w") as f:
            f.write(transcription)
        st.success(f"Transcription saved at {transcription_file_path}")
        return transcription
    except Exception as e:
        return f"Error in transcription: {str(e)}"
    

def get_gpt_response(prompt):
    """Send the transcribed text to GPT-4 model and get a response."""
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": str(prompt)}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()  # Return GPT-4 response
    except Exception as e:
        return f"Error in GPT-4 response: {str(e)}"
