import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from api.models import IMEIRequest
from api.utils import check_imei_imeicheck
from fastapi import HTTPException
from dotenv import load_dotenv
load_dotenv()


TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WHITELIST_USERS = [int(user_id) for user_id in os.getenv("WHITELIST_USERS", "").split(",")] if os.getenv("WHITELIST_USERS") else []


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    if user_id in WHITELIST_USERS:
        await message.answer("Привет! Отправь мне IMEI для проверки.")
    else:
        await message.answer("Вы не авторизованы для использования бота.")


@dp.message(F.text)
async def handle_imei(message: types.Message):
    user_id = message.from_user.id
    if user_id in WHITELIST_USERS:
        imei = message.text
        try:
            imei_req = IMEIRequest(imei=imei)
        except ValueError as e:
            await message.answer(f"Ошибка: {e}")
            return
        try:
           imei_info = check_imei_imeicheck(imei_req.imei)
           await message.answer(str(imei_info))
        except HTTPException as e:
            await message.answer(str(e.detail))
    else:
        await message.answer("Вы не авторизованы для использования бота.")

async def main():
    try:
        await dp.start_polling(bot)
    finally:
      await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
