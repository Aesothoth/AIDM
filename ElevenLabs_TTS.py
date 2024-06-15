Nicole = "piTKgcLEGmPE4e6mEKli"
ADAM = "pNInz6obpgDQGcFmaJgB"
#You will have to change this to add new voices
API_KEY = "Your Elevenlabs API Key here"


import os
from typing import IO
from io import BytesIO
from elevenlabs import VoiceSettings, stream
from elevenlabs.client import ElevenLabs
import requests

def GetVoices():
    url = "Link to your voice here"
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    #Make a GET request to retrieve the voice data
    response = requests.get(url, headers=headers)

    # Handle the response data
    if response.status_code == 200:
        pass
        # Process the voice data as needed
    else:
        print('Failed to retrieve voice data. Status code:', response.status_code)




def text_to_speech_stream(text: str, api_key) -> IO[bytes]:
    client = ElevenLabs(api_key=api_key)
    # Perform the text-to-speech conversion  
    response = client.generate(
        text=text,
        voice=Nicole, # This is where you change the voice (Adam is a stock voice)
        stream=True)

    stream(response)


if __name__ == "__main__":
    GetVoices()
    text_to_speech_stream("Hello World!", API_KEY)
