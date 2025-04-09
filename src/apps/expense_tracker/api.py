from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.apps.expense_tracker import crud
from src.apps.expense_tracker.database import get_db
from src.apps.expense_tracker.schemas import (
    ArticleCreate,
    ArticleRead,
    ArticleUpdate,
)

router = APIRouter()

@router.post("/", response_model=ArticleRead)
def create_article(article_data: ArticleCreate, db: Session = Depends(get_db)):
    return crud.create_article(article_data, db)


@router.get("/", response_model=list[ArticleRead])
def get_articles(db: Session = Depends(get_db)):
    return crud.get_articles(db)


@router.get("/{article_id}/", response_model=ArticleRead)
def get_article(article_id: int, db: Session = Depends(get_db)):
    article = crud.get_article(article_id, db)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@router.patch("/{article_id}/", response_model=ArticleRead)
def update_article(article_id: int, article_data: ArticleUpdate, db: Session = Depends(get_db)):
    article = crud.update_article(article_id, article_data, db)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@router.delete("/{article_id}/", response_model=ArticleRead)
def delete_article(article_id: int, db: Session = Depends(get_db)):
    article = crud.delete_article(article_id, db)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article
