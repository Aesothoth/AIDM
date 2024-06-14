VOICE = "jsCqWAovK2LkecY7zXl4"
VOICE2 = "RisC0PdfB4kk6ANQrosL"
KNIGHTLY = "XvGc31UwFR8EZNcQiq4T"
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
    url = "https://elevenlabs.io/app/voice-lab/share/899444b1d9eab0cea6d20686befafde9ccdc46ab4628e79973cf318a9497b138/fV5Pa91BEdDNCQu0TwZf"
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
        voice=ADAM,
        stream=True)
    try:
        #If you have mpv, you can just stream the response directly (a bit faster)
        stream(response)
    except:
        #If you don't have mpv, you must do this to stream the response
        audio_stream = BytesIO()
        for chunk in response:
            if chunk:
                audio_stream.write(chunk)
        audio_stream.seek(0)
        return audio_stream


if __name__ == "__main__":
    
    GetVoices()
    text_to_speech_stream("Hello World!", API_KEY)
