#Generative AI stuff
import google.generativeai as genai
import json
from gtts import gTTS
import pyttsx3
import keyboard
import time
#Speech-To-Text
from RealtimeSTT import AudioToTextRecorder


def start_recording():
    print("Say something...")
def end_recording():
    print("Recording Ended")
def recording_timeout():
    print("Recording timed out.")
def ConvertJSON(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

stop_phrases = ["I'm done here.", "Canoodle", "Beam me up, Scotty.", "Did I stutter?", "Be me up, Scotty.", "Beat me up, Scotty.", "End voice transmission.", "And voice transmission.", "And the voice transmission."]
SYSTEM_INSTRUCTIONS = f"You are ADAM, a dungeon master in a game of Dungeons and Dragons. Your job is to tell the story of the adventure. You will take your players through a magical adventure through the Forgotten Realms. The adventure will start in a tavern where the two adventurers meet each other. While telling this story, you must always follow these rules: "
RULES = ["1) You must create many NPCs to populate your world.", "2) You must play the part of each creature other than the two players.","3) You may not make decisions for the players, only the NPCs. You may, however, decide what happens due to the actions that the players take.", "4) You must occasionally force the players to make a skill check of some sort."]
API_KEY = "AIzaSyC3UKclriUg_KsFkd2ZeVZyrR3x3g01GIc"
ACTIVATION_KEY = "f4"
for rule in RULES:
    SYSTEM_INSTRUCTIONS += rule

def generate_message(model, message, history):
    engine = pyttsx3.init()
    engine.setProperty('voice', engine.getProperty('voices')[0].id)
    history.append({"role": "user", "parts": message})
    response = model.generate_content(history).text
    history.append({"role": "model", "parts": response})
    model._system_instruction
    print("\n")
    print(response)
    engine.say(response)
        
    dump = json.dumps(history, indent=2)
    with open("history.json", 'w') as file:
        file.write(dump)
    engine.runAndWait()
    return history

def DM_w_SST(recorder):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest', system_instruction=SYSTEM_INSTRUCTIONS)
    history = ConvertJSON("history.json")

    message = ""
    while (True):
        message = ""
        #wait until user presses "f4" key
        print(f"Press {ACTIVATION_KEY} to talk")
        key = keyboard.read_key()

        if key == "esc":
            break
        if key != ACTIVATION_KEY:
            time.sleep(0.1)
            continue

        text = recorder.text()
        while text not in stop_phrases:
            print(text)
            message += (text + " ")
            text = recorder.text()
        print(message)
        history = generate_message(model, message, history)
    

if __name__ == '__main__':
    recorder = AudioToTextRecorder(spinner=False, model="tiny.en", language="en", on_vad_detect_start=start_recording, on_recording_stop=end_recording, on_wakeword_timeout=recording_timeout,post_speech_silence_duration=0.3)
    DM_w_SST(recorder)
    recorder.shutdown()