import speech_recognition as sr
from views.display import display_message

class STTModule:
    def __init__(self):
        self.microfone = sr.Recognizer()

    def capturar_audio(self):    
        while True:
            try:
                with sr.Microphone() as source:
                    print('Escutando...')
                    audioCapturado = self.microfone.listen(source)
                    comandoReconhecido = self.microfone.recognize_google(audioCapturado, language='pt-BR')
                    comandoReconhecido = comandoReconhecido.lower()

                    print("Comando capturado: " + comandoReconhecido)
                    return comandoReconhecido
            except sr.UnknownValueError:
                display_message('Não foi possível te entender. Diga novamente...')
            except sr.RequestError as e:
                display_message(f'Erro de requisição com o serviço de reconhecimento de fala: {e}. Tentando novamente...')
                print(f'Erro de requisição com o serviço de reconhecimento de fala: {e}. Tentando novamente...')
            except Exception as err:
                display_message('Erro inesperado ao capturar o áudio. Tentando novamente...')
                print('Erro inesperado ao capturar o áudio.')
                print(err)
