from controllers.speech_to_text import STTModule
from controllers.text_to_speech import TTSModule
from pynput import keyboard
import threading
import time

def processar_audio():
    stt_module = STTModule()
    comando = stt_module.capturar_audio()
    if comando:
        print(f"Comando recebido: {comando}")
        TTSModule(comando)
    else:
        print("Nenhum comando recebido.")

def on_press(key):
    try:
        # Verifica se a tecla pressionada é a tecla 'Espaço'
        if key == keyboard.Key.space:
            print("Tecla Espaço pressionada.")
            processar_audio()
    except AttributeError:
        pass

def escutar_tecla():
    print('Escutando a tecla espaço...')
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def main():
    print('EVA iniciada')
    TTSModule('Olá eu sou a Eva')

    # Cria e inicia a thread que escuta a tecla R
    thread_escuta_tecla = threading.Thread(target=escutar_tecla)
    thread_escuta_tecla.daemon = True  # Faz com que a thread seja encerrada quando o programa principal terminar
    thread_escuta_tecla.start()

    # Mantém o programa principal em execução
    try:
        while True:
            time.sleep(1)  # Pequena pausa para reduzir o uso da CPU no loop principal
    except KeyboardInterrupt:
        print("Programa encerrado.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
