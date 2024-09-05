# eva-stt-tts

Módulo responsável por realizar o processo de STT e TTS da assistente virtual EVA

```docker
docker build -t amaralfelipe1522/eva-stt-tts:2.0 .
```

```
xhost +local:docker
```

```docker
docker run -it --rm --name eva\
    --device /dev/snd \
    --group-add audio \
    -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e PULSE_SERVER=unix:/run/user/$(id -u)/pulse/native \
    -v /run/user/$(id -u)/pulse/native:/run/user/$(id -u)/pulse/native \
    amaralfelipe1522/eva-stt-tts:2.0
```

-----------------------

A instalação do FFmpeg pode variar dependendo do sistema operacional que você está utilizando. Aqui estão algumas maneiras comuns de instalar o FFmpeg em diferentes sistemas:

Windows:
Baixar o FFmpeg Binaries: Você pode baixar os binários do FFmpeg para Windows no site oficial: https://ffmpeg.org/download.html. Baixe o arquivo ZIP correspondente à sua arquitetura (32 ou 64 bits).

Extrair os arquivos: Após baixar o arquivo ZIP, extraia seu conteúdo para um diretório de sua escolha.

Adicionar ao PATH: Para usar o FFmpeg de qualquer lugar no seu sistema, você precisa adicionar o diretório onde os binários do FFmpeg foram extraídos ao PATH do sistema. Você pode fazer isso nas configurações de ambiente do Windows.

winget install "FFmpeg (Essentials Build)"

sudo apt install ffmpeg

sudo apt install portaudio19-dev python3-dev

## TO DO

- Melhorar PROMPTs 
    - Testar recentes alterações relacionadas a rolagem de dados;
- Melhorar logs
- Armazenar no Mongodb o resumo da ultima sessão (conversation_history);
- Importar o resumo salvo no MongoDB para entrar como PROMPT e continuar de onde parou;
- Criar microserviço a parte para comunicação com banco de dados relacional;