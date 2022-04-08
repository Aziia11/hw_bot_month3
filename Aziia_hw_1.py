from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

from config import bot, dp

@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hello {message.from_user.full_name}")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Hi")

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("WELLDONE!!! CONTINUE",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    question = "What kind of languages in IT you know?"
    answers = [
        "English", "Chinese", "Python", "Turkish"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Surely, great Python))",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )

@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("WELLDONE!!! CONTINUE",
                                         callback_data="button_call_2")
    markup.add(button_call_2)
    question = "What is Python's place in popularity in IT world?"
    answers = [
        "1", "2", "3", "4", "5"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="God's favourite number xo xo",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )

@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("WELLDONE!!! CONTINUE",
                                         callback_data="button_call_3")
    markup.add(button_call_3)
    question = "What does # mean in Python"
    answers = [
        "comments",
        "function",
        "method",
        "anonymous func",
        "to make a code more beautiful"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )

dp.callback_query_handler(lambda call: call.data == "button_call_3")
async def quiz_4(call: types.CallbackQuery):
    question = "Choose the right function:"
    answers = [
        "len(my_list)",
        "from math import sqrt",
        "list_of_squares = list(squares)",
        "def sum_slt(lst):\nsum = lst + lst\nprint(sum)",
        "-1"
    ]
    photo = open("media/photo.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Even,I don't know myself,joking",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


