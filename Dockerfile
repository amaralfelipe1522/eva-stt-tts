# Usa uma imagem base do Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Cria um usuário não-root
RUN useradd -ms /bin/sh appuser

# Instala as dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    libasound2-dev \
    portaudio19-dev \
    libportaudio2 \
    libportaudiocpp0 \
    libffi-dev \
    build-essential \
    alsa-utils \
    pulseaudio \
    x11-apps \
    libx11-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências listadas em requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Instala PyAudio
RUN pip install pyaudio

# Copia o código fonte da aplicação para o diretório de trabalho
COPY . .

# Ajusta permissões dos arquivos e diretório para o usuário não-root
RUN chown -R appuser:appuser /app

# Muda para o usuário não-root
USER appuser

# Define o comando padrão para executar a aplicação
CMD ["python3", "main.py"]
