from openpyxl import Workbook
from pathlib import Path
from datetime import datetime
from src.apps.expense_tracker.models import Article


def generate_report(articles: list[Article]) -> Path:
    wb = Workbook()
    ws = wb.active
    ws.title = "Expense Report"

    ws.append(["ID", "Name", "Date", "Amount (UAH)", "Amount (USD)"])

    for article in articles:
        ws.append([
            article.id,
            article.name,
            article.date.strftime("%Y-%m-%d") if article.date else "",
            float(article.amount),
            float(article.amount_usd),
        ])

    filename = f"expense_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx"
    filepath = Path("reports") / filename
    filepath.parent.mkdir(parents=True, exist_ok=True)

    wb.save(filepath)
    return filepath
