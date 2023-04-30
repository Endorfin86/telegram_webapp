from aiogram import executor
from create_bot import dp
from config import URL_APP
from create_bot import bot
import os

async def on_startup(dp):
    await bot.set_webhook(URL_APP)
    print('Бот запущен')

async def on_shutdown(dp):
    await bot.delete_webhook()


from handlers import client
client.register_handlers_client(dp)

executor.start_webhook(
    dispatcher=dp,
    webhook_path='',
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host="0.0.0.0",
    port=4000
    )