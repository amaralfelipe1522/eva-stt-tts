import json
import os
import openai
from dotenv import load_dotenv
import requests
import utils.prompts as prompt
import re as regex

load_dotenv()

conversation_history = []

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

    global conversation_history

    if len(conversation_history) > 50:
        total = len(conversation_history)
        exceeded = total - 50
        for i in range(1, exceeded):
            conversation_history.pop(i)

    try:     
        url = 'https://perfect-violently-pig.ngrok-free.app/api/chat'
        headers = {
            'Content-Type': 'application/json'
        }        
        
        conversation_history.append({'role': 'user', 'content': input})

        data = {
            'model': 'llama3.1',
            'messages': conversation_history,
            'stream': True
        }

        accumulated_response = ''
        with requests.post(url, headers=headers, json=data, stream=True) as response:
            if response.status_code == 200:
                for line in response.iter_lines():
                    if line:
                        ai_response = json.loads(line.decode('utf-8'))
                        accumulated_response += ai_response["message"]["content"]

                        if regex.search(r'(?: |\.\n?)$', accumulated_response) and not regex .search(r' \d', accumulated_response[-3:]) and not accumulated_response.endswith('...'):
                            conversation_history.append({'role': 'assistant', 'content': accumulated_response})
                            yield accumulated_response
                            accumulated_response = ''

                if accumulated_response:
                    conversation_history.append({'role': 'assistant', 'content': accumulated_response})
                    yield accumulated_response
            else:
                yield 'Erro em se conectar com a I.A Generativa'
        
    except Exception as e:
        print(f'Ocorreu um erro na comunicação com o Ollama: {e}')
        yield f'Ocorreu um erro: {e}'

def get(ai_name, input):
    """
    Seleciona e chama a IA generativa com base no nome fornecido.

    Parâmetros:
    ai_name: Nome da IA generativa a ser chamada ('ollama' ou 'chatgpt').
    input: Texto ou prompt que será enviado à IA selecionada.

    Retorna:
    Resposta gerada pela IA ou uma mensagem de erro se a IA não for encontrada.
    """
    if ai_name == 'ollama':
         return get_ollama(input)
    elif ai_name == 'chatgpt':
         return get_chatgpt(input)
    else:
         return 'Nenhuma I.A generativa selecionada'