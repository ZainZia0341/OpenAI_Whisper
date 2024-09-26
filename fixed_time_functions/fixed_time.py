import openai
import sounddevice as sd
import numpy as np
import soundfile as sf
import os
from dotenv import load_dotenv

load_dotenv()

# Set your OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def record_audio(duration, fs, output_file, device=1):
    """Record audio from the microphone and save it to a file."""
    if device is None:
        device = sd.default.device[0]  # Default to system input device if not specified
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16', device=device)
    sd.wait()  # Wait until the recording is finished
    sf.write(output_file, audio_data, fs)
    return output_file


def transcribe_audio(file_path):
    """Send audio to OpenAI Whisper for transcription."""
    try:
        with open(file_path, "rb") as audio_file:
            response = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return response  # Return the transcription text
    except Exception as e:
        return f"Error in transcription: {str(e)}"
    

def get_gpt_response(prompt):
    """Send the transcribed text to GPT-4 model and get a response."""
    try:
        response = openai.chat.completions.create(
            model="gpt-4",  # Change this to your actual model name if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": str(prompt)}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()  # Return GPT-4 response
    except Exception as e:
        return f"Error in GPT-4 response: {str(e)}"