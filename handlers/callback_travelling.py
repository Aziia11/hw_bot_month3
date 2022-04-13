from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

from config import bot

async def travelling(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_9 = InlineKeyboardButton("The world is a book and those who don't travel read only one page.",
                                         callback_data="button_call_9")
    button_call_10 = InlineKeyboardButton("Only two things we will regret on deathbed"
                                          " – that we are a little loved and little traveled.",
                                         callback_data="button_call_10")
    markup.add(button_call_9, button_call_10)
    await bot.send_message(call.message.chat.id, 'U are lucky',
                           reply_markup=markup)

async def travelling_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_11 = InlineKeyboardMarkup("Afferend sana!",
                                         callback_data = "button_call_11")
    markup.add(button_call_11)
    question = "Who is the author of the quote\n" \
               "Travel as the greatest science and serious science helps us to rediscover ourselves."
    answers = [
        "Putin",
        "Zelenskiy",
        " Mark Twain",
        "Albert Camus",
        "Marc Levy"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='travelling',
        correct_option_id=3,
        explanation="",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )

def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(travelling,
                                       lambda call: call.data == "button_call_8")
    dp.register_callback_query_handler(travelling_1,
                                       lambda call: call.data == "button_call_10")