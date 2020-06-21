from subprocess import Popen
from subprocess import PIPE

import time
from logging import getLogger

from Chat_Features.buttons import *
from Core.Commands.dict import *

from Settings.config import load_config
commands_config = load_config()
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
        text = messages['HELLO'],
    )

@debug_request
def keyboard(bot,update):
    global KEYBOARD_STATE
    KEYBOARD_STATE = False if KEYBOARD_STATE else True
    bot.send_message(
        chat_id = update.message.chat_id,
        text = messages['KEYBOARD'] + ("enabled" if KEYBOARD_STATE else "disabled"),
        reply_markup = show_base_reply_keyboard() if KEYBOARD_STATE else remove_base_reply_keyboard(),
    )

@debug_request
def help(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = messages['HELP']
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
    elif text == HIDE_KEYBOARD_BUTTON:
        return keyboard(bot,update)
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
    bot.sendMessage(
        chat_id = update.message.chat_id,
        text = text
    )

@debug_request
def server_time(bot, update):
    tmp_time = round( time.time() - start_time, 4 )
    bot.sendMessage(
        chat_id = update.message.chat_id,
        text = str(tmp_time) + messages['TIME']
    )
