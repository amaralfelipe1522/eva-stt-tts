# syntax=docker/dockerfile:1

FROM python:latest

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /eva-stt-tts

RUN apt-get update -y && \
    apt-get -y install --no-install-recommends \
        python3-pyaudio \
        libespeak1 \
        alsa-tools \
        libsndfile1-dev \
        pulseaudio-module-jack \
        alsa-utils && \
    pip install --upgrade pip && \
    pip install pyttsx3==2.71 \
    SpeechRecognition

COPY . .

CMD [ "python", "index.py" ]