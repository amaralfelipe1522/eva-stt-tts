import speech_recognition as sr
from gtts import gTTS
import pygame
from io import BytesIO
from pydub import AudioSegment, effects

microfone = sr.Recognizer()
        
print('EVA iniciada')

try:
    with sr.Microphone() as source:
        # microfone.adjust_for_ambient_noise(source)
        print('Escutando...')
        audioCapturado = microfone.listen(source)
        comando = microfone.recognize_google(audioCapturado, language='pt-BR')
        comando = comando.lower()

        print("Comando capturado: " + comando)

        comando = 'eva Vocês se encontram na entrada da pequena vila de Alderspring, onde a última luz do sol pinta o céu em tons de laranja e púrpura. As primeiras estrelas começam a aparecer, pontilhando o firmamento com promessas de mistérios por descobrir. O vento carrega o cheiro de pão recém-assado, misturado com o aroma da terra molhada da recente chuva de primavera.'
            
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
    print('Audio não foi capturado...')
    print(err)