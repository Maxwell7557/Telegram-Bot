from subprocess import Popen

from telegram import Bot
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

from config import TG_TOKEN
from config import TG_API_URL

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

def time(bot, update):
    print('Time called')
    process = Popen(stdout=subprocess.PIPE)
    data = process.communicate()
    print(data)
    bot.send_message(
        chat_id = update.message.chat_id,
        text = data
    )

def main():
    bot = Bot(token = TG_TOKEN, base_url = TG_API_URL,)
    updater = Updater(bot = bot,)

    start_handler = CommandHandler('start',start)
    help_handler = CommandHandler('help',help)
    time_handler = CommandHandler('time',time)

    message_handler = MessageHandler(Filters.text,echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(time_handler)

    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
