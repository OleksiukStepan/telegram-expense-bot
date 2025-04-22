import httpx
import os
from dotenv import load_dotenv

from src.config import API_BASE_URL

load_dotenv()

API_EXPENSES_URL = f"{API_BASE_URL}/expenses/"


async def submit_expense(data: dict) -> tuple[bool, str]:
    payload = {
        "name": data["name"],
        "amount": float(data["amount"]),
        "date": data["date"].isoformat(),
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{API_EXPENSES_URL}", json=payload)

        if response.status_code in (200, 201):
            return True, "✅ Витрату збережено успішно!"
        return False, f"❌ Помилка {response.status_code}: {response.text}"
    except Exception as e:
        return False, f"⚠️ Виникла помилка: {e}"
