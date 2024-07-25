import speech_recognition as sr
import pygame
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment, effects

print('EVA iniciada')

def sttModule():    
    try:
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            print('Escutando...')
            # microfone.adjust_for_ambient_noise(source)
            audioCapturado = microfone.listen(source)
            comandoReconhecido = microfone.recognize_google(audioCapturado, language='pt-BR')
            comandoReconhecido = comandoReconhecido.lower()

            print("Comando capturado: " + comandoReconhecido)
            # comandoReconhecido = 'eva Vocês se encontram na entrada da pequena vila de Alderspring, onde a última luz do sol pinta o céu em tons de laranja e púrpura.
            return comandoReconhecido
    except Exception as err:
        print('Audio não foi capturado...')
        print(err)

comando = sttModule()

def ttsModule(comando):
    try:
        if 'eva' in comando:
            comando = comando.replace('eva', '', 1)
            # Cria um objeto gTTS
            tts = gTTS(text=comando, lang='pt-br')

            # Salva a saída em um buffer de memória
            buffer = BytesIO()
            tts.write_to_fp(buffer)
            buffer.seek(0)

            # Carrega o buffer de memória como um AudioSegment
            audio = AudioSegment.from_file(buffer, format="mp3")

            # Ajusta a velocidade do áudio
            audio = audio.speedup(playback_speed=1.4)

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
                continue
        
        # if 'erva' in comando:
        # if 'evelyn' in comando:
        # if 'ela' in comando:

    except Exception as err:
        print('Não foi possível reproduzir o áudio...')
        print(err)

ttsModule(comando)