from datetime import datetime, date
from typing import Optional


def validate_date(date_str: str, fmt: str = "%Y-%m-%d") -> Optional[date]:
    try:
        return datetime.strptime(date_str, fmt).date()
    except ValueError:
        return None
