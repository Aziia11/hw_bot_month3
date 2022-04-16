from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import user_kb
from config import bot

class FSMADMIN_register(StatesGroup):
    id = State()
    username = State()
    first_name = State()
    last_name = State()

async def is_user_command(message: types.Message):
    global ID
    ID = message.chat.id
    await bot.send_message(message.chat.id,
                           "Yes, user\n"
                           "Subscribe,for my bot ",
                           reply_markup=user_kb.button_user)
    await message.delete()

async def cancel_command(message: types.Message,
                         state: FSMContext):
    if message.chat.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return "State is None, Relax"
        await state.finish()
        await message.reply("Canceled Successfully")



async def load_id(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as info:
        info['id'] = message.chat.id
    await FSMADMIN_register.next()
    await message.reply("User, Send me your username please 😉 ")


async def load_username(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as info:
        info['username'] = message.text
    await FSMADMIN_register.next()
    await message.reply("User, Send me your first_name please 😌")


async def load_first_name(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as info:
        info['first_name'] = message.text
    await FSMADMIN_register.next()
    await message.reply("User, Send me your last_name please 🙂")

async def load_last_name(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as info:
        info['last_name'] = message.text
    await FSMADMIN_register.next()
    await message.reply("Your application is accepted 👍")
    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()


def register_handler_user(dp: Dispatcher):
    dp.register_message_handler(is_user_command, commands=['register_user'])
    dp.register_message_handler(cancel_command, state='*', commands=['Отмена'])
    dp.message_handler(cancel_command, Text(equals='cancel', ignore_case=False), state='*')
    dp.register_message_handler(load_id, state=FSMADMIN_register.id)
    dp.register_message_handler(load_username, state=FSMADMIN_register.username)
    dp.register_message_handler(load_first_name, state=FSMADMIN_register.first_name)
    dp.register_message_handler(load_last_name, state=FSMADMIN_register.last_name)

