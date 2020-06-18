from subprocess import Popen
from subprocess import PIPE

import time
from logging import getLogger

from telegram import Bot
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

from Settings.config import load_config
from Chat_Features.buttons import *

config = load_config()
logger = getLogger(__name__)

start_time = time.time()

def debug_request(f):
    def inner (*args, **kwargs):
        try:
            logger.info(f'/{f.__name__}')
            return f(*args, **kwargs)
        except Exception:
            logger.exception(f'/{f.__name__}')
            raise
    return inner


@debug_request
def start(bot,update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = 'Hello there!',
    )

@debug_request
def keyboard(bot,update):
    global KEYBOARD_STATE
    KEYBOARD_STATE = False if KEYBOARD_STATE else True
    bot.send_message(
        chat_id = update.message.chat_id,
        text = f'Keyboard {"enabled" if KEYBOARD_STATE else "disabled"}',
        reply_markup = show_base_reply_keyboard() if KEYBOARD_STATE else remove_base_reply_keyboard(),
    )

@debug_request
def help(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = 'There will be a full description of bot commands soon! \n'
    )

@debug_request
def echo(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    if text == HELP_BUTTON:
        return help(bot,update)
    elif text == REAL_TIME_BUTTON:
        return cur_time(bot,update)
    elif text == SERVER_TIME_BUTTON:
        return server_time(bot,update)
    else:
        reply_text = f"Your ID = {chat_id}\n\n{update.message.text}"
        bot.send_message(
            chat_id = update.message.chat_id,
            text = reply_text,
        )

@debug_request
def cur_time(bot, update):
    process = Popen('date',stdout=PIPE)
    text, err = process.communicate()
    text = text.decode('utf-8')
    print('>    ' + text)
    bot.sendMessage(
        chat_id = update.message.chat_id,
        text = text
    )

@debug_request
def server_time(bot, update):
    tmp_time = round( time.time() - start_time, 4 )
    print('>    ' + str(tmp_time) + '  seconds')
    bot.sendMessage(
        chat_id = update.message.chat_id,
        text = str(tmp_time) + ' seconds'
    )

def main():
    bot = Bot(token = config.TG_TOKEN, base_url = config.TG_API_URL,)
    updater = Updater(bot = bot,)

    start_handler = CommandHandler('start',start)
    help_handler = CommandHandler('help',help)
    cur_time_handler = CommandHandler('cur_time',cur_time)
    server_time_handler = CommandHandler('server_time',server_time)
    keyboard_handler = CommandHandler('keyboard',keyboard)
    message_handler = MessageHandler(Filters.text,echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(cur_time_handler)
    updater.dispatcher.add_handler(server_time_handler)
    updater.dispatcher.add_handler(keyboard_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
