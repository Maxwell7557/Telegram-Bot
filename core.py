from telegram import Bot
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

from Settings.config import *
from Core.Commands.commands import *

config = commands_config
path = find_path()

def handle():
    bot = Bot(
        token=config.TG_TOKEN,
        # base_url = config.TG_API_URL,
    )
    updater = Updater(
        bot=bot,
    )

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    cur_time_handler = CommandHandler('cur_time', cur_time)
    server_time_handler = CommandHandler('server_time', server_time)
    keyboard_handler = CommandHandler('keyboard', keyboard)
    message_handler = MessageHandler(Filters.text, echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(cur_time_handler)
    updater.dispatcher.add_handler(server_time_handler)
    updater.dispatcher.add_handler(keyboard_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    handle()
