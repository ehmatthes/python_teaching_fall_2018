from gtts import gTTS

import os

def say_something(msg):
    tts = gTTS(text=msg, lang='en')
    tts.save('msg.mp3')
    os.system('start msg.mp3')
