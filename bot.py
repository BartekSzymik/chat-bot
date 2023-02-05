# bot.py
from chatterbot import ChatBot

chatbot = ChatBot("Chatpot")

exit_condition = (':q', 'quit', 'exit')
while True:
    query = input('> ')
    if query in exit_condition:
        break
    else:
        print(f'Chatpot 🪴 {chatbot.get_response(query)}')
