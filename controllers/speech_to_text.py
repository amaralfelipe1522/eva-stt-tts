import speech_recognition as sr
from views.display import display_message

class STTModule:
    def __init__(self):
        self.microfone = sr.Recognizer()

    def capturar_audio(self):    
        try:
            with sr.Microphone() as source:
                print('Escutando...')
                audioCapturado = self.microfone.listen(source)
                comandoReconhecido = self.microfone.recognize_google(audioCapturado, language='pt-BR')
                comandoReconhecido = comandoReconhecido.lower()

                print("Comando capturado: " + comandoReconhecido)
                return comandoReconhecido
        except Exception as err:
            display_message('Audio não foi capturado...')
            print('Audio não foi capturado...')
            print(err)
            return None
