FROM python:3.10.8

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /eva-stt-tts

RUN adduser $(whoami) audio && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends \
    # multimedia-jack \
    # jackd2 \
    libasound-dev \
    libportaudio2 \
    libportaudiocpp0 \
    portaudio19-dev \
    libsndfile1 \
    alsa-utils \
    build-essential portaudio19-dev && \
    # python3-pyaudio && \
    pip3 install --upgrade pip && \
    pip3 install SpeechRecognition \
    pyttsx3 \
    PyAudio
    # dpkg-reconfigure -p high jackd2 \

COPY . .

CMD [ "python" ]