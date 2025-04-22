from aiogram import Router, F
from aiogram.types import Message
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
    await message.answer(" Яка дата витрати?")


@router.message(StateFilter(ExpenseForm.date))
async def process_date(message: Message, state: FSMContext):
    user_date = validate_date(message.text)

    if not user_date:
        await message.answer("❌ Невірний формат дати. Спробуй ще раз у форматі YYYY-MM-DD.")
        return

    await state.update_data(date=user_date)

    data = await state.get_data()
    success, msg = await submit_expense(data)
    await message.answer(msg)

    await state.clear()
