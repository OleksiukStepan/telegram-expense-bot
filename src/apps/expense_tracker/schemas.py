from datetime import date
from typing import Optional

from pydantic import BaseModel


class ArticleBase(BaseModel):
    name: str
    date: Optional[date] = None
    amount: float


class ArticleCreate(ArticleBase):
    ...


class ArticleRead(ArticleBase):
    id: int
    date: date
    amount_usd: float

    class Config:
        orm_mode = True


class ArticleUpdate(ArticleBase):
    name: Optional[str] = None
    date: Optional[date] = None
    amount: Optional[float] = None
