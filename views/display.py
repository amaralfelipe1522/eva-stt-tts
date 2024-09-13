from controllers.text_to_speech import TTSModule
import re as regex

def display_message(message):
    TTSModule(message)
    print(regex.sub(r'^\s+|(?<=\d\.)\n+', '', message))
