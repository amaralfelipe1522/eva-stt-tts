import pygame
import boto3 # type: ignore
from dotenv import load_dotenv # type: ignore
import os

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
            print('Não foi possível reproduzir o áudio...')
            print(err)
        finally:
            pygame.mixer.quit()
