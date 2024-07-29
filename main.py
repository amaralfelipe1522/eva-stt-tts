import speech_recognition as sr
import pygame
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment, effects

class TTSModule:
    def __init__(self, comando):
        try:
            # Cria um objeto gTTS
            tts = gTTS(text=comando, lang='pt-br')

            # Salva a saída em um buffer de memória
            buffer = BytesIO()
            tts.write_to_fp(buffer)
            buffer.seek(0)

            # Carrega o buffer de memória como um AudioSegment
            audio = AudioSegment.from_file(buffer, format="mp3")

            # Ajusta a velocidade do áudio
            audio = audio.speedup(playback_speed=1.3)

            # Normaliza o áudio
            audio = effects.normalize(audio)

            # Converte o áudio de volta para o formato de buffer de memória
            buffer = BytesIO()
            audio.export(buffer, format="mp3")
            buffer.seek(0)

            # Inicializa o mixer do pygame
            pygame.mixer.init()

            # Carrega o buffer de memória como um stream
            pygame.mixer.music.load(buffer)

            # Reproduz o áudio
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as err:
            print('Não foi possível reproduzir o áudio...')
            print(err)
        finally:
            pygame.mixer.quit()

class STTModule:
    def __init__(self):
        self.microfone = sr.Recognizer()  

    def capturar_audio(self):    
        try:
            with sr.Microphone() as source:
                print('Escutando...')
                # microfone.adjust_for_ambient_noise(source)
                audioCapturado = self.microfone.listen(source)
                comandoReconhecido = self.microfone.recognize_google(audioCapturado, language='pt-BR')
                comandoReconhecido = comandoReconhecido.lower()

                print("Comando capturado: " + comandoReconhecido)
                # comandoReconhecido = 'eva Vocês se encontram na entrada da pequena vila de Alderspring, onde a última luz do sol pinta o céu em tons de laranja e púrpura.
                return comandoReconhecido
        except Exception as err:
            TTSModule('Audio não foi capturado...')
            print('Audio não foi capturado...')
            print(err)

def main():
    
    print('EVA iniciada')

    TTSModule('Olá eu sou a Eva, o que você gostaria de falar?')

    stt_module = STTModule()
    comando = stt_module.capturar_audio()

    # if 'eva' in comando:
        # comando = comando.replace('eva', '', 1)
            # if 'erva' in comando:
            # if 'evelyn' in comando:
            # if 'ela' in comando:

    TTSModule(comando)

if __name__ == "__main__":
    main()