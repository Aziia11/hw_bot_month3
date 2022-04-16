from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_register = KeyboardButton('/subscribe')
button_can = KeyboardButton('/Отмена')

button_user = ReplyKeyboardMarkup(
    resize_keyboard=True).row(button_register, button_can)