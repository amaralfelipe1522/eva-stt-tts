# eva-stt-tts

Módulo responsável por realizar o processo de STT e TTS da assistente virtual EVA

```docker
docker build -t amaralfelipe1522/eva-stt-tts:1.0 .
```

```docker
docker run --rm -it --name eva-tts-stt amaralfelipe1522/eva-stt-tts:1.0 sh
```

```docker
docker run --rm -it --device /dev/snd --name eva-tts-stt amaralfelipe1522/eva-stt-tts:1.0 sh
```

pip install PyAudio

pip install pywhatkit

pip install pyttsx3

pip install wikipedia

pip install SpeechRecognition

-----------------------

A instalação do FFmpeg pode variar dependendo do sistema operacional que você está utilizando. Aqui estão algumas maneiras comuns de instalar o FFmpeg em diferentes sistemas:

Windows:
Baixar o FFmpeg Binaries: Você pode baixar os binários do FFmpeg para Windows no site oficial: https://ffmpeg.org/download.html. Baixe o arquivo ZIP correspondente à sua arquitetura (32 ou 64 bits).

Extrair os arquivos: Após baixar o arquivo ZIP, extraia seu conteúdo para um diretório de sua escolha.

Adicionar ao PATH: Para usar o FFmpeg de qualquer lugar no seu sistema, você precisa adicionar o diretório onde os binários do FFmpeg foram extraídos ao PATH do sistema. Você pode fazer isso nas configurações de ambiente do Windows.

winget install "FFmpeg (Essentials Build)"