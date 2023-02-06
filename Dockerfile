# syntax=docker/dockerfile:1

FROM python:latest

WORKDIR /eva-stt-tts

RUN pip install --upgrade pip && \
    pip3 install SpeechRecognition && \
    pip3 install pyttsx3 && \
    apt-get update -y && \
    apt-get install python3-pyaudio -y

COPY . .

CMD [ "python3", "-v"]