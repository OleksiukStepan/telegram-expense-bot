from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Додати витрату")],
            [KeyboardButton(text="📄 Отримати звіт")],
        ],
        resize_keyboard=True
    )
    await message.answer(
        "👋 Привіт! Це бот для обліку витрат.\nОберіть дію нижче:",
        reply_markup=keyboard
    )
