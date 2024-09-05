from pynput import keyboard
from controllers import generativeAI_selector
from controllers.speech_to_text import STTModule
from views.display import display_message

def processar_audio():
    stt_module = STTModule()
    comando = stt_module.capturar_audio() 
    if comando:
        for resposta in generativeAI_selector.get('ollama', comando):
            display_message(resposta)
    else:
        print("Nenhum comando recebido.")
                 
def on_press(key):
    try:
        if key == keyboard.Key.space:
            print("Tecla Espaço pressionada.")
            processar_audio()
        # criar nova variante de tecla esperada
    except AttributeError:
        pass

def start_listening():
    print('Escutando a tecla espaço...')
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
