import os
from dotenv import load_dotenv
import telebot
from telebot.types import Message


load_dotenv('.env')
my_token = os.getenv('TELEGRAM_BOT_TOKEN')
bot_client = telebot.TeleBot(token=my_token)


@bot_client.message_handler(commands=["start"])
def echo(message: Message):
    bot_client.send_message(chat_id=message.chat.id, text='''Подписывайтесь на телеграм-канал t.me/YariqGunesTravel
    Добро пожаловать на http://github.com/YaroslavLovtsov''')


if __name__ == "__main__":
    bot_client.polling()
