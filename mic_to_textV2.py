'''primero instalar estos paquetes en local:
pip install SpeechRecognition
pip install gtts
pip install pyaudio'''

import speech_recognition as sr
import os

recognizer = sr.Recognizer()

try:
    #listado de mics disponibles
    print("micrófonos disponibles:")
    print(sr.Microphone.list_microphone_names())
    
    #selecciono el micrófono que voy a usar
    with sr.Microphone(device_index=1) as source:
        print("ajustando niveles de ruido...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Grabando audio de 4 segungos...")
        recorded_audio = recognizer.listen(source, timeout=4)
        print("Grabación realizada.")
    #convertimos la grabación en texto
    try:
        print("reconociendo el texto...")
        text = recognizer.recognize_google_cloud(recorded_audio, language="es-US")
        print("Texto decodificado: {}".format(text))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
except Exception as ex:
    print("Error during recognition:", ex)


