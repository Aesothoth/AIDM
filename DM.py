#Generative AI stuff
import google.generativeai as genai
import json
import keyboard
import time
import os
#Speech-To-Text
from RealtimeSTT import AudioToTextRecorder
from ElevenLabs_TTS import text_to_speech_stream



# Utility Functions
def vad_start():
    print("Say something...")
def end_recording():
    print("Recording Ended")
def start_recording():
    print("Recording ...")
def recording_timeout():
    print("Recording timed out.")
def ConvertJSON(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

# Optional to change these
stop_phrases = ["I'm done here.", "Canoodle", "Beam me up, Scotty.", "Did I stutter?", "Be me up, Scotty.", "Beat me up, Scotty.", "End voice transmission.", "And voice transmission.", "And the voice transmission.", "Stop transmission.", "Stop voice transmission."]
SYSTEM_INSTRUCTIONS = f"You are ADAM, a dungeon master in a game of Dungeons and Dragons. Your job is to tell the story of the adventure. You will take your players through a magical adventure through the Forgotten Realms. The adventure will start in a tavern where the two adventurers meet each other. While telling this story, you must always follow these rules: "
RULES = ["1) You must create many NPCs to populate your world.", "2) You must play the part of each creature other than the two players.","3) You may not make decisions for the players, only the NPCs. You may, however, decide what happens due to the actions that the players take.", "4) When the user asks to make a skill check, you must set a reasonable DC, then roll the d20 to determine the result.", "5) When addressed as Adam, you may respond as the DM instead of as one of the NPCs.", "6) You must occasionally make up and use fantasy swears."]
for rule in RULES:
    SYSTEM_INSTRUCTIONS += rule

ACTIVATION_KEY = "f4"
TERMINATION_KEY = "esc"


# You will have to change these to get your thing to work
ELEVENLABS_KEY = "Your Elevenlabs API Key here"
API_KEY = "Your Gemini API Key here"



def generate_message(message, model):
    history = ConvertJSON("history2.json")
    history.append({"role": "user", "parts": message})
    try:
        response = model.generate_content(history).text
        history.append({"role": "model", "parts": response})
        print("\n")
        print(response)
        text_to_speech_stream(response, ELEVENLABS_KEY)
    
        dump = json.dumps(history, indent=2)
        with open("history2.json", 'w') as file:
            file.write(dump)
    except:
        print("Response generation failed")
        

def DM_w_SST(recorder):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest', system_instruction=SYSTEM_INSTRUCTIONS)
    while (True):
        #wait until user presses "f4" key
        print(f"Press {ACTIVATION_KEY} to talk or {TERMINATION_KEY} to end")
        key = keyboard.read_key()

        if key == TERMINATION_KEY:
            break
        if key != ACTIVATION_KEY:
            time.sleep(0.1)
            continue
        message = recorder.text()
        print(message)
        generate_message(message, model)
    

if __name__ == '__main__':
    recorder = AudioToTextRecorder(spinner=False, model="tiny.en", language="en", on_vad_detect_start=vad_start, on_recording_start=start_recording, on_recording_stop=end_recording, on_wakeword_timeout=recording_timeout,post_speech_silence_duration=2)
    DM_w_SST(recorder)
    recorder.shutdown()
