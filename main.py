from controllers.speech_to_text import STTModule
from controllers.text_to_speech import TTSModule

def main():
    print('EVA iniciada')
    TTSModule('Olá eu sou a Eva, o que você gostaria de falar?')

    stt_module = STTModule()
    comando = stt_module.capturar_audio()

    if comando:
        TTSModule(comando)

if __name__ == "__main__":
    main()