from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot


def conversation():
    chatting = []
    archive = open('chat.txt', 'r')
    for var in archive:
        chatting.append(var.replace('\n',''))
    return chatting


bot = ChatBot('Suporte',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              database_uri='sqlite:///database.sqlite3')

chatting = conversation()

print(chatting)

chat = ListTrainer(bot)
chat.train(chatting)

#while True:
#    try:
#        resposta = bot.get_response(input("Usuário: "))
#        if float(resposta.confidence) > 2:
#            print("bot ", resposta)
#        else:
#            print("Eu não entendi :(")
#    except(KeyboardInterrupt, EOFError, SystemExit):
#        break



