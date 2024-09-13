# Usa uma imagem base do Python
FROM cgr.dev/chainguard/python:latest-dev as builder

USER root

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="eva-stt-tts/venv/bin:$PATH"

# Define o diretório de trabalho dentro do container
WORKDIR /eva-stt-tts

RUN apk update && apk add --no-cache bash
# Instala as dependências do sistema
RUN apk update && apk add \
    ffmpeg \
    alsa-lib-dev \
    portaudio-dev \
    libffi-dev \
    pulseaudio-utils \
    build-base \
    && rm -rf /var/cache/apk/*

# Dependências para acessar o servidor X11 
RUN apk update && apk add \
    libx11 \
    xauth \
    && rm -rf /var/cache/apk/*

# Copia o arquivo requirements.txt para o diretório de trabalho
RUN python -m venv /eva-stt-tts/venv
COPY requirements.txt .

# Instala as dependências listadas em requirements.txt
RUN /eva-stt-tts/venv/bin/pip install --no-cache-dir -r requirements.txt

# Instala PyAudio
RUN /eva-stt-tts/venv/bin/pip install pyaudio

# Copia o código fonte da aplicação para o diretório de trabalho
# COPY . .



FROM cgr.dev/chainguard/python:latest
USER root

WORKDIR /eva-stt-tts

ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"

COPY --from=builder /eva-stt-tts/venv /venv
# COPY main.py ./
COPY . ./

# Define o comando padrão para executar a aplicação

ENTRYPOINT [ "/venv/bin/python","/eva-stt-tts/main.py" ]
