# Installation:
## 1)
Open ElevenLabs_TTS.py

Change API_KEY to your elevenlabs API key
## 2)
Open DM.py

Change API_KEY to your gemini API key

Change ELEVENLABS_KEY to your elevenlabs API key
## 3)
Open the file in the command terminal (Ask me if you don't know how)

Type "venv\Scripts\activate.bat" into the terminal

Type "python Elevenlabs_TTS.py" into the terminal

## 4)
Go to https://mpv.io/

Install mpv to this folder

# Use:
Open the file in the command terminal (Ask me if you don't know how)

Type "venv\Scripts\activate.bat" into the terminal

Type "python DM.py" into the terminal

Press "f4" to start talking to the bot or "escape" to end the conversation

## If you want to add voices from your Elevenlabs account (Only need to do once for each voice):
Open Elevenlabs_TTS.py 

Change the value of url to the url of the voice you want to add in the GetVoices() function

Change the value of voice to the VoiceID of the voice you want in the text_to_speech_stream() function
