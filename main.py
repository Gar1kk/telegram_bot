import asyncio
import os
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiohttp import web
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


# Обработчик Webhook
async def handle_webhook(request):
    data = await request.json()
    update = dp.feed_update(bot, data)
    return web.Response(text="ok")


# Главная функция
async def main():
    await set_commands()

    # Получаем URL сервера
    render_url = os.getenv("RENDER_EXTERNAL_URL")
    if not render_url:
        render_url = "http://localhost:8000"

    webhook_url = f"{render_url}/webhook"

    # Устанавливаем Webhook
    await bot.set_webhook(webhook_url)
    print(f"✅ Webhook установлен на {webhook_url}")

    # Создаём веб-приложение
    app = web.Application()
    app.router.add_post("/webhook", handle_webhook)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8000)
    await site.start()

    print("✅ Бот запущен на порту 8000! 🚀")

    # Бесконечный цикл
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())