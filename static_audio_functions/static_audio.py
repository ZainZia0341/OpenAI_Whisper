# app.py
import openai
import io
from pydub import AudioSegment
from dotenv import load_dotenv
import os

load_dotenv()

# Set your OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def save_uploaded_file(uploaded_file):
    """
    Save uploaded file temporarily and return the path.
    """
    temp_file_path = os.path.join("temp_audio_file.mp3")
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())  # Save the in-memory buffer to a file
    return temp_file_path


def transcribe_audio(audio_file_path):
    try:
        # Open the MP3 file directly
        with open(audio_file_path, "rb") as audio_file:
            # Transcribe with Whisper (MP3 is a supported format)
            response = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return response

    except Exception as e:
        return f"Error in transcription: {str(e)}"
    

def get_gpt_response(prompt):
    print("Prompt: ", prompt)
    
    # Call OpenAI GPT-4 API
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": str(prompt)}  # Ensure the prompt is passed as a string
        ],
        max_tokens=150
    )
    return response.choices[0].message.content.strip()

