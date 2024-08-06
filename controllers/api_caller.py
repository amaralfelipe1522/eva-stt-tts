import os
import openai
from dotenv import load_dotenv
import utils.prompts as prompt

load_dotenv()

# def get():
#     try:
#         request = requests.get("https://viacep.com.br/ws/08773535/json/")
#         responseJSON = json.loads(request.content)
#         return responseJSON['localidade']
#     except Exception as e:
#         print(f"Ocorreu um erro na chamada da API: {e}")

def get_chatgpt(input = 'greeting'):
        try:
            openai_api_key = os.getenv("OPENAI_API_KEY")
            openai.api_key = openai_api_key

            if input not in locals():
                roles = [{"role": "system", "content": prompt.prompt_dnd}]
            else:
                roles.append({"role": "user", "content": input})

            # [
            #     {"role": "system", "content": "Você é um assistente útil."},
            #     {"role": "user", "content": "Quais são as funcionalidades da API do ChatGPT?"}
            #     {"role": "assistant", "content": "A capital da Itália é Roma."},
            # ],

            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",  # gpt-4 ou gpt-3.5-turbo
                messages=roles,
                max_tokens=100,  # Limite o tamanho da resposta
                n=1,  # Número de respostas
                stop=[".", "\n"],  # Define a sequência de parada. Ex.: stop=[".", "\n"] ou stop=None
                temperature=0.5,  # Ajuste a criatividade da resposta
            )

            ia_response = response['choices'][0]['message']['content']
            roles.append({"role": "assistant", "content": ia_response})

            print("ia_response > ", ia_response)
            return ia_response

        except Exception as e:
            print(f"Ocorreu um erro na comunicação com o ChatGPT: {e}")
