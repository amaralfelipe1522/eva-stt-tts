from controllers.text_to_speech import TTSModule

def display_message(message):
    TTSModule(message)
    print(message)
