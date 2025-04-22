import asyncio
from src.apps.telegram.bot import bot, dp
from src.apps.telegram.handlers import start


async def main():
    dp.include_router(start.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
