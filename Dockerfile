FROM python:3.10.6

WORKDIR /eva-stt-tts

RUN apt-get update -y && \
    apt-get -y install --no-install-recommends \
    python3-pyaudio && \
    pip3 install --upgrade pip && \
    pip3 install SpeechRecognition \
    pyttsx3

COPY . .

CMD [ "python" ]