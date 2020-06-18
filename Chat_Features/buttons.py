from telegram import ReplyMarkup
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

KEYBOARD_STATE = False

HELP_BUTTON = 'Help'
REAL_TIME_BUTTON = 'Current Time'
SERVER_TIME_BUTTON = 'Server Time'

def show_base_reply_keyboard():
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

class remove_base_reply_keyboard(ReplyMarkup):
    def __init__(self, selective=False, **kwargs):
        self.remove_keyboard = True
        self.selective = bool(selective)
