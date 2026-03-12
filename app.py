import sounddevice as sd
import numpy as np
import whisper
import keyboard
import ollama
import pyautogui
import time

SAMPLE_RATE = 16000
DURATION = 10

print("loading whisper model")
model = whisper.load_model("base")
print("Hold ctrl+space and speak")
def record_audio():
    print("listening")
    audio = sd.rec(int(DURATION * SAMPLE_RATE),
                   samplerate=SAMPLE_RATE,
                   channels=1,
                   dtype='float32')
    
    sd.wait()
    print("got it!!!")
    return audio.flatten()

def transcribe(audio):
    result = model.transcribe(audio,fp16 = False)
    text = result['text'].strip()
    print(f"you said:{text}")
    return text


def ask_ollama(text):
    response = ollama.chat(
        model='llama3',
        messages=[{
            'role': 'system',
            'content': '''You control a Windows PC using Python.
When given a command, reply with ONLY raw Python code. No explanation. No markdown.
Use these rules:
- To open websites: import webbrowser; webbrowser.open("url")
- To open apps: import subprocess; subprocess.Popen("app.exe")
- To type text: import pyautogui; pyautogui.write("text")
- To press keys: import pyautogui; pyautogui.press("key")
- To click: import pyautogui; pyautogui.click(x, y)
- Always add: import time; time.sleep(1) between actions'''
        },
        {
            'role': 'user',
            'content': text
        }]
    )
    return response['message']['content']


def execute(code):
    print("executing")
    try:
        exec(code)
    except Exception as e:
        print(f"error : {e}")


def run():
    audio = record_audio()
    text = transcribe(audio)

    if text:
        code = ask_ollama(text)
        print(f"AI SAYs : \n{code}")
        execute(code)


keyboard.add_hotkey('ctrl+space', run)
keyboard.wait()