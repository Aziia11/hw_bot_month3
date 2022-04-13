from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from keyboards import client_kb
from config import bot


async def hello(message: types.Message):
    await message.reply(text="Hello")
    await bot.send_message(message.chat.id,
                           f"Hello {message.from_user.full_name}",
                           reply_markup=client_kb.start_markup)

async def help(message: types.Message):
    await message.reply("1. /quiz command will start quiz series of problems\n"
                        "Whenever U press Welldone!!! CONTINUE will appear next quiz\n"
                        "Note: Bot-Admin will delete cursed words,so that's why be careful")

async def game(message: types.Message):
    await message.reply("2. /game command will start quiz about game\n"
                        "Whenever U press U are great GAMER will appear next quiz\n"
                        "Note: Bot-Admin will delete cursed words,so that's why be careful😛")

async def inform(message: types.Message):
    await message.reply("3. /info command will appear all information about bot\n"
                        "who created it and other aspects.")

async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Welldone!!! CONTINUE",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    question = "What is the most popular language in IT in the last years?"
    answers = [
        "JAVA", "C++", "PYTHON", "JAVASCRIPT", "UX/UI DESIGNER"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Surely,Python",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(game, commands=['game'])
    dp.register_message_handler(inform, commands=['info'])
