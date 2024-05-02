'''primero instalar estos paquetes en local:
pip install SpeechRecognition
pip install gtts'''

import speech_recognition as sr
import os

recognizer = sr.Recognizer()


#listado de mics disponibles
print("micrófonos disponibles:")
print(sr.Microphone.list_microphone_names())