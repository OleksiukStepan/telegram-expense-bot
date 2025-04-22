import asyncio
from src.apps.telegram.bot import bot, dp
from src.apps.telegram.handlers import start, expense


async def main():
    dp.include_router(start.router)
    dp.include_router(expense.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
