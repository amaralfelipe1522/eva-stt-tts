import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
maquina = pyttsx3.init()

maquina.say('EVA inicializada')

print('****************')


try:
    with sr.Microphone() as source:
        print('EVA está te ouvindo...')
        voz = audio.listen(source)

        comando = audio.recognize_google(voz, language='pt-BR')
        comando = comando.lower()

        if 'eva' in comando:
            print(comando)
            maquina.say(comando)
            maquina.runAndWait()


except:
    print('Audio não foi capturado...')