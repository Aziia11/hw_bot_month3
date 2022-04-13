from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

from config import bot

async def fasting_quiz_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_6 = InlineKeyboardMarkup("Afferend sana!",
                                         callback_data="button_call_6")
    markup.add(button_call_6)
    question = "Are U fasting?"
    answers = [
        "much works",
        "yes,many sins",
        "yes,to get slim",
        "none",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='fasting_quiz',
        correct_option_id=3,
        explanation="It was a joke 😋",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


async def fasting_quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_7 = InlineKeyboardButton("Afferend sana!",
                                         callback_data="button_call_7")
    markup.add(button_call_7)
    question = "What does this picture means"
    answers = [
        "birth_date calendar",
        "bad_days calendar",
        "fasting calendar",
        "calendar of gym"
    ]
    photo = open("media/photo12.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='fasting_quiz',
        correct_option_id=2,
        explanation="You did it ",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


async def fasting_quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_8 = InlineKeyboardMarkup("Afferend sana!",
                                         callback_data="button_call_8")
    markup.add(button_call_8)
    question = "What is recommended to eat the most in Ramadan months?"
    answers = [
        "dates",
        "cucumber",
        "lettuce",
        "banana",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='fasting_quiz',
        correct_option_id=0,
        explanation="no comments",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        # reply_markup=markup,
    )


def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(fasting_quiz_1,
                                       lambda call: call.data == "button_call_5")
    dp.register_callback_query_handler(fasting_quiz_2,
                                       lambda call: call.data == "button_call_6")
    dp.register_callback_query_handler(fasting_quiz_3,
                                       lambda call: call.data == "button_call_7")
