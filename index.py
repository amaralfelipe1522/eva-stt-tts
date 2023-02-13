import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
maquina = pyttsx3.init()

print('EVA iniciada')

def iniciarComando():
    try:
        with sr.Microphone() as source:
            print('Escutando...')
            voz = audio.listen(source)

            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()

            if 'eva' in comando:
                comando = comando.replace('eva', '', 1)
                maquina.say(comando)
                maquina.runAndWait()
            
            if 'erva' in comando:
                comando = comando.replace('erva', '', 1)
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Audio não foi capturado...')

    return comando

iniciarComando()