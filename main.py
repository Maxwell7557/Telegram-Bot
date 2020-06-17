from subprocess import Popen
from subprocess import PIPE

import time

from telegram import Bot
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

from config import TG_TOKEN
from config import TG_API_URL

start_time = time.time()

def start(bot,update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = 'Hello there!',
    )

def help(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = 'There will be a full description of bot commands soon! \n'
    )

def echo(bot, update):
    chat_id = update.message.chat_id
    text = f"Your ID = {chat_id}\n\n{update.message.text}"
    bot.send_message(
        chat_id = update.message.chat_id,
        text = text,
    )

def cur_time(bot, update):
    process = Popen('date',stdout=PIPE)
    text, err = process.communicate()
    text = text.decode('utf-8')
    bot.sendMessage(
        chat_id = update.message.chat_id,
        text = text
    )

def server_time(bot, update):
    tmp_time = round( time.time() - start_time, 4 )
    print(tmp_time)
    bot.sendMessage(
        chat_id = update.message.chat_id,
        text = str(tmp_time) + ' seconds'
    )

def main():
    bot = Bot(token = TG_TOKEN, base_url = TG_API_URL,)
    updater = Updater(bot = bot,)

    start_handler = CommandHandler('start',start)
    help_handler = CommandHandler('help',help)
    cur_time_handler = CommandHandler('cur_time',cur_time)
    server_time_handler = CommandHandler('server_time',server_time)

    message_handler = MessageHandler(Filters.text,echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(cur_time_handler)
    updater.dispatcher.add_handler(server_time_handler)

    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
