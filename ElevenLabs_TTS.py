API_KEY = "a0ad55c0440f52030743d34c0d31f6b0"
VOICE = "jsCqWAovK2LkecY7zXl4"
VOICE2 = "RisC0PdfB4kk6ANQrosL"
KNIGHTLY = "XvGc31UwFR8EZNcQiq4T"
ADAM = "pNInz6obpgDQGcFmaJgB"

import os
from typing import IO
from io import BytesIO
from elevenlabs import VoiceSettings, stream
from elevenlabs.client import ElevenLabs
import requests

def GetVoices():
    url = "https://elevenlabs.io/app/voice-lab/share/899444b1d9eab0cea6d20686befafde9ccdc46ab4628e79973cf318a9497b138/fV5Pa91BEdDNCQu0TwZf"
    headers = {
        'Authorization': 'Bearer a0ad55c0440f52030743d34c0d31f6b0',
        'Content-Type': 'application/json'
    }

    #Make a GET request to retrieve the voice data
    response = requests.get(url, headers=headers)

    # Handle the response data
    if response.status_code == 200:
        voice_data = response.json()
        # Process the voice data as needed
    else:
        print('Failed to retrieve voice data. Status code:', response.status_code)
    return voice_data




def text_to_speech_stream(text: str, api_key) -> IO[bytes]:
    client = ElevenLabs(api_key=api_key)
    # Perform the text-to-speech conversion
    response = client.generate(
        text=text,
        voice=KNIGHTLY,
        stream=True)

    # Create a BytesIO object to hold the audio data in memory
    audio_stream = BytesIO()

    # Write each chunk of audio data to the stream
    for chunk in response:
        if chunk:
            audio_stream.write(chunk)

    # Reset stream position to the beginning
    audio_stream.seek(0)

    # Return the stream for further use
    stream(audio_stream)

if __name__ == "__main__":
    text_to_speech_stream("Hello World!")
