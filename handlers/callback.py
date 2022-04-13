from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

from config import bot



async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("WELLDONE!!! CONTINUE",
                                         callback_data="button_call_2")
    markup.add(button_call_2)

    question = "By whom invented Python?"
    answers = [
        "Harry Potter", "Putin", "Voldemort", "Linus Tervalds", "Guido Van Rossum"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="Great Guido Van Rossum",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("WELLDONE!!! CONTINUE",
                                         callback_data="button_call_3")
    markup.add(button_call_3)
    question = "What is Python's place in popularity in IT world?"
    answers = [
        "1", "2", "3", "4", "5"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="God's favourite number xo xo",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

async def quiz_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("WELLDONE!!! CONTINUE",
                                         callback_data="button_call_4")
    markup.add(button_call_4)
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

async def quiz_5(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_5 = InlineKeyboardButton("WELLDONE!!! CONTINUE",
                                         callback_data="button_call_5")
    markup.add(button_call_5)
    question = "What kind of sort this?"
    answers = [
        "selection sort",
        "quick sort",
        "bubble sort",
        "insertion sort",
        "merge sort"
    ]
    photo = open("media/photo11.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="You did it ",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        #reply_markup=markup,
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2,
                                       lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3,
                                       lambda call: call.data == "button_call_2")
    dp.register_callback_query_handler(quiz_4,
                                       lambda call: call.data == "button_call_3")
    dp.register_callback_query_handler(quiz_5,
                                       lambda call: call.data == "button_call_4")