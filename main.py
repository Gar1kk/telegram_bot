import asyncio
import os
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand, BotCommandScopeDefault
from handlers import router

# Загружаем TOKEN из .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN не найден в .env файле!")

# Создаём бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Добавляем обработчики
dp.include_router(router)

# Устанавливаем команды бота
async def set_commands():
    commands = [
        BotCommand(command="start", description="Главное меню"),
        BotCommand(command="about", description="О нас"),
        BotCommand(command="bonuses", description="Бонусная программа"),
        BotCommand(command="help", description="Связь с нами"),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

# Главная функция
async def main():
    await set_commands()
    print("✅ Бот запущен! 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())