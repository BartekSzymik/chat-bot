# bot.py
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from cleaner import clean_corpus

CORPUS_FILE = 'chat.txt'

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)


exit_condition = (':q', 'quit', 'exit')
while True:
    query = input('> ')
    if query in exit_condition:
        break
    else:
        print(f'Chatpot 🪴 {chatbot.get_response(query)}')
