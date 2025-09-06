import logging
from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = os.getenv("BOT_TOKEN")  # Токен из Environment Variables Railway

# Настройка логов
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# --- Обработчики ---
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я работаю на Railway 24/7!")

# --- Запуск бота ---
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
