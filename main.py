import logging
from aiogram import Bot, Dispatcher, executor, types
import requests
from os import getenv
from qrCode import create_qr_code


API_TOKEN = '5133148009:AAFS1ptLb0xYEjmMUNIiwbVo-JHtkcMmnIM'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("""QrCode yasash botiga xush kelibsiz!\n Botdan foydalanish uchun tekst yoki havolani kiriting. \n va u sizga qr kodni yuboradi.""")


@dp.message_handler()
async def text_to_qr(message: types.Message):
    text = message.text
    width = 200
    height = 200
    qr_code = create_qr_code(text, width, height)
    await bot.send_photo(message.chat.id, qr_code)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
