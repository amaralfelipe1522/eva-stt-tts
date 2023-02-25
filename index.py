import speech_recognition as sr
import pyttsx3

microfone = sr.Recognizer()
engine = pyttsx3.init('dummy')

print('EVA iniciada')

try:
    with sr.Microphone() as source:
        # microfone.adjust_for_ambient_noise(source)
        print('Escutando...')
        audioCapturado = microfone.listen(source)

        comando = microfone.recognize_google(audioCapturado, language='pt-BR')
        comando = comando.lower()

        print("Comando capturado: " + comando)
            
        if 'eva' in comando:
            comando = comando.replace('eva', '', 1)
            engine.say(comando)
            engine.runAndWait()
        
        if 'erva' in comando:
            comando = comando.replace('erva', '', 1)
            engine.say(comando)
            engine.runAndWait()

        if 'evelyn' in comando:
            comando = comando.replace('evelyn', '', 1)
            engine.say(comando)
            engine.runAndWait()

        if 'ela' in comando:
            comando = comando.replace('ela', '', 1)
            engine.say(comando)
            engine.runAndWait()

except Exception as err:
    print('Audio não foi capturado...')
    print(err)