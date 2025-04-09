from typing import Type, List

from sqlalchemy.orm import Session

from src.apps.expense_tracker.models import Article
from src.apps.expense_tracker.schemas import ArticleCreate, ArticleUpdate
from src.apps.expense_tracker.utils import get_usd_exchange_rate


def get_articles(db: Session) -> list[Type[Article]]:
    return db.query(Article).all()


def get_article(article_id: int, db: Session) -> Type[Article] | None:
    return db.query(Article).filter(Article.id == article_id).first()


def create_article(article: ArticleCreate, db: Session) -> Article:
    exchange_rate = get_usd_exchange_rate()
    amount_usd = float(article.amount) / exchange_rate

    db_article = Article(
        name=article.name,
        date=article.date,
        amount=article.amount,
        amount_usd=round(amount_usd, 2),
    )

    db.add(db_article)
    db.commit()
    db.refresh(db_article)

    return db_article


def update_article(
    article_id: int,
    article_data: ArticleUpdate,
    db: Session
) -> Type[Article] | None:
    db_article = db.query(Article).filter(Article.id == article_id).first()

    if not db_article:
        return None

    for key, value in article_data.dict(exclude_unset=True).items():
        setattr(db_article, key, value)

    db.commit()
    db.refresh(db_article)

    return db_article


def delete_article(article_id: int, db: Session) -> Type[Article] | None:
    db_article = db.query(Article).filter(Article.id == article_id).first()

    if not db_article:
        return None

    db.delete(db_article)
    db.commit()

    return db_article
