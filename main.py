from aiogram.utils import executor
from config import dp
from handlers import client, callback, extra, callback_fasting, callback_travelling,fsmadmin,fsmadmin_register
from database import bot_db


async def on_startup(_):
    bot_db.sql_create()
    print("Bot is online!")

fsmadmin.register_handler_admin(dp)
fsmadmin_register.register_handler_user(dp)
client.register_handlers_client(dp)
callback_fasting.register_handler_callback(dp)
callback_travelling.register_handler_callback(dp)
callback.register_handlers_callback(dp)
extra.register_handlers_other(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)