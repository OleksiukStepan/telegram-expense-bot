from datetime import date

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from src.apps.telegram.services.expense_service import submit_expense
from src.apps.telegram.states.expense import ExpenseForm
from src.apps.telegram.validators.date import validate_date

router = Router()

@router.message(F.text == "➕ Додати витрату")
async def add_expense_start(message: Message, state: FSMContext):
    await message.answer("📝 Як називається витрата?")
    await state.set_state(ExpenseForm.name)


@router.message(StateFilter(ExpenseForm.name))
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ExpenseForm.amount)
    await message.answer("💰 Яка сума витрати?")


@router.message(StateFilter(ExpenseForm.amount))
async def process_amount(message: Message, state: FSMContext):
    await state.update_data(amount=message.text)
    await state.set_state(ExpenseForm.date)
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Сьогодні")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await message.answer(
        "📅 Яка дата витрати?\n"
        "Введи у форматі: <b>YYYY-MM-DD</b>\n"
        "Або натисни <b>кнопку нижче</b>, щоб використати сьогоднішню дату:",
        parse_mode="HTML",
        reply_markup=keyboard
    )


@router.message(StateFilter(ExpenseForm.date))
async def process_date(message: Message, state: FSMContext):
    text = message.text.strip()

    if text == "Сьогодні":
        user_date = date.today()
    else:
        user_date = validate_date(text)
        if not user_date:
            await message.answer(
                f"❌ Невірний формат {text}. Спробуй так: <b>2025-04-23</b>",
                parse_mode="HTML"
            )
            return

    await state.update_data(date=user_date)

    data = await state.get_data()
    success, msg = await submit_expense(data)
    await message.answer(msg)

    await state.clear()
