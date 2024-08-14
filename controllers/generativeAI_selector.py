import os
import openai
from dotenv import load_dotenv
import requests
import utils.prompts as prompt

load_dotenv()

def get_chatgpt(input = 'greeting'):
        try:
            openai_api_key = os.getenv('OPENAI_API_KEY')
            openai.api_key = openai_api_key

            if input not in locals():
                roles = [{'role': 'system', 'content': prompt.prompt_test}]
            else:
                roles.append({'role': 'user', 'content': input})

            # Exemplo:
            # [
            #     {'role': 'system', 'content': 'Você é um assistente útil.'},
            #     {'role': 'user', 'content': 'Quais são as funcionalidades da API do ChatGPT?'}
            #     {'role': 'assistant', 'content': 'A capital da Itália é Roma.'},
            # ],

            response = openai.chat.completions.create(
                model='gpt-3.5-turbo',  # gpt-4 ou gpt-3.5-turbo
                messages=roles,
                max_tokens=100,  # Limite o tamanho da resposta
                n=1,  # Número de respostas
                stop=['.', '\n'],  # Define a sequência de parada. Ex.: stop=['.', '\n'] ou stop=None
                temperature=0.5,  # Ajuste a criatividade da resposta
            )

            ai_response = response['choices'][0]['message']['content']
            roles.append({'role': 'assistant', 'content': ai_response})

            print('ai_response > ', ai_response)
            return ai_response

        except Exception as e:
            print(f'Ocorreu um erro na comunicação com o ChatGPT: {e}')

def get_ollama(input):
    try:     
        url = 'https://perfect-violently-pig.ngrok-free.app/api/generate'
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'model': 'llama3.1',
            'prompt': input,
            'stream': False
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            ai_response = response.json()
            return ai_response['response']
        else:
            return 'Erro em se conectar com a I.A Generativa'
        
    except Exception as e:
            print(f'Ocorreu um erro na comunicação com o Ollama: {e}')

def get(ai_name: str, input: str) -> str:
    """
    Seleciona e chama a IA generativa com base no nome fornecido.

    Parâmetros:
    ai_name (str): Nome da IA generativa a ser chamada ('ollama' ou 'chatgpt').
    input (str): Texto ou prompt que será enviado à IA selecionada.

    Retorna:
    str: Resposta gerada pela IA ou uma mensagem de erro se a IA não for encontrada.
    """
    if ai_name == 'ollama':
         return get_ollama(input)
    elif ai_name == 'chatgpt':
         return get_chatgpt(input)
    else:
         return 'Nenhuma I.A generativa selecionada'