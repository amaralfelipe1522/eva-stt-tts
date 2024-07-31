import json
import requests

def get():
            try:
                request = requests.get("https://viacep.com.br/ws/08773535/json/")
                responseJSON = json.loads(request.content)
                # print(responseJSON['localidade'])
                return responseJSON['localidade']
            except Exception as e:
                print(f"Ocorreu um erro na chamada da API: {e}")