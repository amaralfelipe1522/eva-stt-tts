import pygame
import boto3 # type: ignore
from dotenv import load_dotenv # type: ignore
import os
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment, effects

load_dotenv()

secret_key = os.getenv("AWS_ACCESS_KEY_ID")
database_url = os.getenv("AWS_SECRET_ACCESS_KEY")

class TTSModule:
    def __init__(self, comando):
        try:

            # Configurando a sessão do boto3 com as credenciais da AWS
            polly_client = boto3.Session(
                aws_access_key_id=secret_key,
                aws_secret_access_key=database_url,
                region_name='us-west-2'
            ).client('polly')

            # Fazendo a chamada ao Polly para sintetizar o texto
            response = polly_client.synthesize_speech(
                Text=comando,
                OutputFormat='mp3',
                VoiceId='Camila'
            )

            # Salvando o arquivo de áudio
            with open('speech.mp3', 'wb') as file:
                file.write(response['AudioStream'].read())

            # Reproduz o arquivo de áudio
            pygame.mixer.init()
            pygame.mixer.music.load('speech.mp3')
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as err:
            print('text_to_speech.py > Erro no serviço de TTS Polly da AWS')
            print(err)
            TTSModuleFREE(comando)
        finally:
            pygame.mixer.quit()

class TTSModuleFREE:
    def __init__(self, comando):
        try:
            tts = gTTS(text=comando, lang='pt-br')

            buffer = BytesIO()
            tts.write_to_fp(buffer)
            buffer.seek(0)

            audio = AudioSegment.from_file(buffer, format="mp3")
            audio = audio.speedup(playback_speed=1.3)
            audio = effects.normalize(audio)

            buffer = BytesIO()
            audio.export(buffer, format="mp3")
            buffer.seek(0)

            pygame.mixer.init()
            pygame.mixer.music.load(buffer)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as err:
            print('text_to_speech.py > Erro no serviço de TTS gTTS da Google')
            print(err)
        finally:
            pygame.mixer.quit()
