from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo


web_app = WebAppInfo(url="https://endorfin86.github.io/")
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Запустить приложение', web_app=web_app)]
    ],
    resize_keyboard=True)