from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot(
    'Мой Помощник',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Я пока не знаю, что ответить. Можете переформулировать?',
            'maximum_similarity_threshold': 0.90  
        }
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',  
    database_uri='sqlite:///database.sqlite3' 
)

trainer = ChatterBotCorpusTrainer(chatbot)


# trainer.train('./data/my_corpus.yml')  

# list_trainer = ListTrainer(chatbot)
# list_trainer.train([
#     "Привет", "Здравствуйте!",
#     "Как дела?", "Всё хорошо, спасибо!"
# ])

print("Бот готов к общению. Для выхода введите 'выход'.")
while True:
    try:
        user_input = input("Вы: ")
        if user_input.lower() in ('выход', 'exit', 'quit'):
            print("Бот: До свидания!")
            break
        response = chatbot.get_response(user_input)
        print(f"Бот: {response}")
    except (KeyboardInterrupt, EOFError):
        break