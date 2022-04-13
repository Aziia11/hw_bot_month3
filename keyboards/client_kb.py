from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


help_button = KeyboardButton("/help")
quiz_button = KeyboardButton("/quiz")
game_button = KeyboardButton("/game")
inform_button = KeyboardButton("/inform")
location_button = KeyboardButton("Share Location", request_location=True)
info_button = KeyboardButton("Share Info", request_contact=True)

start_markup = ReplyKeyboardMarkup(resize_keyboard=True)

start_markup.row(help_button, quiz_button, game_button, inform_button, location_button, info_button)