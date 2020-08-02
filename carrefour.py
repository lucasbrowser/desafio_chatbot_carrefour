import telepot
from config.configuracoes import TOKEN_TELEGRAM
from Chatbot import Chatbot

telegram = telepot.Bot(TOKEN_TELEGRAM)
bot = Chatbot("Banco Carrefour")

def main(msg):
    phrase = bot.listen(phrase=msg['text'])
    answer = bot.analyze(phrase)
    bot.talk(answer)
    chatID = msg['chat']['id']
    telegram.sendMessage(chatID, answer)


telegram.message_loop(main)

while True:
    pass
