# syntax=docker/dockerfile:1

FROM python:latest

WORKDIR /eva-stt-tts

RUN pip install --upgrade pip && \
    pip3 install SpeechRecognition && \
    pip install pyttsx3==2.71 && \
    apt-get update -y && \
    apt-get install python3-pyaudio -y && \
    apt-get install libespeak1 -y

COPY . .

CMD [ "python3", "-v"]