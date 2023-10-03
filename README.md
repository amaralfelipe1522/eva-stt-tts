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
