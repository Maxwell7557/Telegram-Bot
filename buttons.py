from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

HELP_BUTTON = 'Help'
REAL_TIME_BUTTON = 'Current Time'
SERVER_TIME_BUTTON = 'Server Time'

def get_base_reply_keyboard():
    keyboard = [
        [
            KeyboardButton(HELP_BUTTON),
            KeyboardButton(REAL_TIME_BUTTON),
            KeyboardButton(SERVER_TIME_BUTTON),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard = keyboard,
        resize_keyboard = True,
    )
