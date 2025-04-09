from datetime import date

from sqlalchemy import Column, String, Date, Numeric, Integer

from src.apps.expense_tracker.database import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    date = Column(Date, default=date.today)
    amount = Column(Numeric(10, 2), nullable=False)
    amount_usd = Column(Numeric(10, 2))
