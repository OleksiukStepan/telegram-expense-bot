from aiogram.fsm.state import State, StatesGroup


class ExpenseForm(StatesGroup):
    name = State()
    amount = State()
    date = State()
