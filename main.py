from controllers import generativeAI_selector
from controllers.input_listener import start_listening
import threading
import time
from views.display import display_message
from utils import prompts

def main():
    print('EVA iniciada')

    display_message('Carregando a aventura.. aguarde um momento..')
    for resposta in generativeAI_selector.get('ollama', prompts.prompt_dnd):
        display_message(resposta)

    # Cria e inicia a thread que escuta a tecla Espaço
    thread_escuta_tecla = threading.Thread(target=start_listening)
    thread_escuta_tecla.daemon = True  # Faz com que a thread seja encerrada quando o programa principal terminar
    thread_escuta_tecla.start()

    # Mantém o programa principal em execução
    try:
        while True:
            time.sleep(1)  # Pequena pausa para reduzir o uso da CPU no loop principal
    except KeyboardInterrupt:
        print('Programa encerrado.')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
