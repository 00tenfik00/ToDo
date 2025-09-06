import logging
from aiogram import Bot, Dispatcher, executor, types
from flask import Flask
from threading import Thread
import os

API_TOKEN = os.getenv("BOT_TOKEN")  # Токен будем хранить в переменных окружения

# Настройка логов
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# --- Flask сервер для Render ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Бот работает!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

# --- Обработчики бота ---
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я работаю на Render 24/7!")

# --- Запуск ---
if __name__ == '__main__':
    keep_alive()
    executor.start_polling(dp, skip_updates=True)
