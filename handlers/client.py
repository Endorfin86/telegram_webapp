from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import keyboard
from config import TOKENPAY
from aiogram.types.message import ContentType
from aiogram.types import InputFile

async def start_command(message: types.Message):
    await message.delete()
    await bot.send_message(message.from_user.id, 'Нажми на кнопку "Запустить приложение", которая находится под строкой ввода сообщения 👇', reply_markup=keyboard)

async def get_web_data(web_app_message):
    data = web_app_message.web_app_data.data
    data = data.split(":")
    await bot.send_message(web_app_message.chat.id, data[0])
    await bot.send_message(web_app_message.chat.id, data[1])
    await bot.send_message(web_app_message.chat.id, data[2], reply_markup=keyboard)

async def invoice_requests(web_app_message):
    data = web_app_message.web_app_data.data
    data = data.split("^")
    PRICE = types.LabeledPrice(label=f"Покупка {data[0]}", amount=int(data[1])*100) # в копейках
    if TOKENPAY.split(':')[1] == 'TEST':

        await bot.send_message(web_app_message.chat.id, 'Тестовый платеж!')
        print(data[2])
        await bot.send_invoice(web_app_message.chat.id,
                            title='Покупка автомобиля',
                            description=f'Преобретаемый автомобиль {data[0]} стоимостью ${data[1]}',
                            provider_token=TOKENPAY,
                            currency='usd',
                            photo_url=data[2],
                            photo_width=257,
                            photo_height=257,
                            photo_size=257,
                            is_flexible=False,
                            prices=[PRICE],
                            start_parameter="one-month-subscription",
                            payload="test-invoice-payload")
        
#предпродажа премиум-доступа
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

#продажа премиум-доступа
async def successful_payment(message: types.Message):
    print("Successful payment:")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")
    await bot.send_message(message.from_user.id, f"Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(invoice_requests, content_types='web_app_data')
    dp.register_pre_checkout_query_handler(pre_checkout_query, lambda query: True)
    dp.register_message_handler(successful_payment, content_types=ContentType.SUCCESSFUL_PAYMENT)