
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(
    token=os.getenv("TOKEN"),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
