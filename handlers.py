from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

router = Router()


# ═══════════════════════════════════════════════════════════════
# ГЛАВНОЕ МЕНЮ
# ═══════════════════════════════════════════════════════════════

def get_main_keyboard():
    """Главное меню с кнопками"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛍️ Магазин", callback_data="shop")],
        [InlineKeyboardButton(text="ℹ️ О нас", callback_data="about")],
        [InlineKeyboardButton(text="🎁 Бонусная программа", callback_data="bonuses")],
        [InlineKeyboardButton(text="📞 Связь с нами", callback_data="help")],
    ])
    return keyboard


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """Команда /start - главное меню"""
    await message.answer(
        "👋 Добро пожаловать в наш магазин одежды!\n\n"
        "Выбери раздел:",
        reply_markup=get_main_keyboard()
    )


# ═══════════════════════════════════════════════════════════════
# МАГАЗИН (МИНИ-АПП)
# ═══════════════════════════════════════════════════════════════

@router.callback_query(F.data == "shop")
async def cb_shop(callback: types.CallbackQuery):
    """Переход в магазин (мини-апп)"""
    # ЗАМЕНИ ТУТ НА СВОЙ БОТ ID И ССЫЛКУ НА МИНИ-АПП
    # Формат: https://t.me/ТВ_БОТ_USERNAME/app_name

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🛍️ Открыть магазин",
            web_app=WebAppInfo(url="https://clothesshop-app.netlify.app")
        )],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_menu")],
    ])

    await callback.message.edit_text(
        "🛍️ Магазин одежды\n\n"
        "Нажми кнопку ниже, чтобы открыть полный каталог товаров "
        "с фильтрацией по полу и категориям!",
        reply_markup=keyboard
    )
    await callback.answer()


# ═══════════════════════════════════════════════════════════════
# О НАС
# ═══════════════════════════════════════════════════════════════

@router.callback_query(F.data == "about")
async def cb_about(callback: types.CallbackQuery):
    """Информация о магазине"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_menu")],
    ])

    await callback.message.edit_text(
        "ℹ️ О нашем магазине\n\n"
        "Добро пожаловать в наш онлайн магазин одежды!\n\n"
        "✨ Мы предлагаем:\n"
        "• Качественную одежду для мужчин и женщин\n"
        "• Актуальные тренды и классические стили\n"
        "• Быструю доставку по всей стране\n"
        "• Гарантию на качество товара\n\n"
        "👥 Наша команда работает для вашего удовлетворения!\n"
        "Мы ценим каждого клиента и стремимся предоставить "
        "лучший сервис.",
        reply_markup=keyboard
    )
    await callback.answer()


# ═══════════════════════════════════════════════════════════════
# БОНУСНАЯ ПРОГРАММА
# ═══════════════════════════════════════════════════════════════

@router.callback_query(F.data == "bonuses")
async def cb_bonuses(callback: types.CallbackQuery):
    """Бонусная программа"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_menu")],
    ])

    await callback.message.edit_text(
        "🎁 Бонусная программа\n\n"
        "Спасибо, что выбираете наш магазин!\n\n"
        "💝 Как это работает:\n"
        "1️⃣ Сделай первый заказ любого размера\n"
        "2️⃣ Получи 20% скидку на второй заказ!\n"
        "3️⃣ Повторяй заказы и наслаждайся скидками\n\n"
        "✅ Условия:\n"
        "• Скидка автоматически применяется на второй заказ\n"
        "• Действует для всех зарегистрированных пользователей\n"
        "• Скидка применяется на всю корзину\n\n"
        "Начни покупать и получай бонусы! 🚀",
        reply_markup=keyboard
    )
    await callback.answer()


# ═══════════════════════════════════════════════════════════════
# СВЯЗЬ С НАМИ / ПОМОЩЬ
# ═══════════════════════════════════════════════════════════════

@router.callback_query(F.data == "help")
async def cb_help(callback: types.CallbackQuery):
    """Связь с нами"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Написать менеджеру", url="https://t.me/garsikkkk")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_menu")],
    ])

    await callback.message.edit_text(
        "📞 Связь с нами\n\n"
        "Есть вопросы или нужна помощь?\n"
        "Свяжись с нашей командой!\n\n"
        "👤 Менеджер: @garsikkkk\n\n"
        "Мы ответим тебе в ближайшее время! ⏱️",
        reply_markup=keyboard
    )
    await callback.answer()


# ═══════════════════════════════════════════════════════════════
# КОМАНДЫ (альтернатива кнопкам)
# ═══════════════════════════════════════════════════════════════

@router.message(Command("about"))
async def cmd_about(message: types.Message):
    """Команда /about"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_menu")],
    ])

    await message.answer(
        "ℹ️ О нашем магазине\n\n"
        "Добро пожаловать в наш онлайн магазин одежды!\n\n"
        "✨ Мы предлагаем:\n"
        "• Качественную одежду для мужчин и женщин\n"
        "• Актуальные тренды и классические стили\n"
        "• Быструю доставку по всей стране\n"
        "• Гарантию на качество товара\n\n"
        "👥 Наша команда работает для вашего удовлетворения!",
        reply_markup=keyboard
    )


@router.message(Command("bonuses"))
async def cmd_bonuses(message: types.Message):
    """Команда /bonuses"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_menu")],
    ])

    await message.answer(
        "🎁 Бонусная программа\n\n"
        "💝 Как это работает:\n"
        "1️⃣ Сделай первый заказ любого размера\n"
        "2️⃣ Получи 20% скидку на второй заказ!\n"
        "3️⃣ Повторяй заказы и наслаждайся скидками",
        reply_markup=keyboard
    )


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    """Команда /help"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Написать менеджеру", url="https://t.me/garsikkkk")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_menu")],
    ])

    await message.answer(
        "📞 Связь с нами\n\n"
        "👤 Менеджер: @garsikkkk\n\n"
        "Мы ответим тебе в ближайшее время! ⏱️",
        reply_markup=keyboard
    )


# ═══════════════════════════════════════════════════════════════
# СПИСОК ВСЕХ КОМАНД
# ═══════════════════════════════════════════════════════════════

@router.message(Command("commands"))
async def cmd_commands(message: types.Message):
    """Показываем список всех доступных команд"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👋 /start", callback_data="back_to_menu")],
        [InlineKeyboardButton(text="ℹ️ /about", callback_data="about")],
        [InlineKeyboardButton(text="🎁 /bonuses", callback_data="bonuses")],
        [InlineKeyboardButton(text="📞 /help", callback_data="help")],
    ])

    await message.answer(
        "📋 Доступные команды:\n\n"
        "🏠 /start - Главное меню\n"
        "ℹ️ /about - О нас\n"
        "🎁 /bonuses - Бонусная программа\n"
        "📞 /help - Связь с нами\n"
        "📋 /commands - Список всех команд\n\n"
        "Или выбери из кнопок ниже:",
        reply_markup=keyboard
    )


# ═══════════════════════════════════════════════════════════════
# КНОПКА НАЗАД
# ═══════════════════════════════════════════════════════════════

@router.callback_query(F.data == "back_to_menu")
async def cb_back_to_menu(callback: types.CallbackQuery):
    """Возврат в главное меню"""
    await callback.message.edit_text(
        "👋 Добро пожаловать в наш магазин одежды!\n\n"
        "Выбери раздел:",
        reply_markup=get_main_keyboard()
    )
    await callback.answer()


# ═══════════════════════════════════════════════════════════════
# ПРОЧИЕ СООБЩЕНИЯ
# ═══════════════════════════════════════════════════════════════

@router.message()
async def echo_handler(message: types.Message):
    """Ловит все остальные сообщения"""
    await message.answer(
        "Я не понимаю эту команду 😅\n\n"
        "Используй /start для главного меню или /commands для списка всех команд",
        reply_markup=get_main_keyboard()
    )