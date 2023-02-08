import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
tts = pyttsx3.init()

tts.say('EVA inicializada')
tts.say('Como posso te ajudar?')
tts.runAndWait()

try:
    with sr.Microphone() as source:
        print('EVA está te ouvindo...')
        voz = audio.listen(source)

        comando = audio.recognize_google(voz, language='pt-BR')
        comando = comando.lower()

        if 'eva' in comando:
            print(comando)


except:
    print('Audio não foi capturado...')