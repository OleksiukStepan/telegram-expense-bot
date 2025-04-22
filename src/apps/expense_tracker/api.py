from datetime import datetime, date
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from src.apps.expense_tracker import crud
from src.apps.expense_tracker.database import get_db
from src.apps.expense_tracker.schemas import (
    ArticleCreate,
    ArticleRead,
    ArticleUpdate,
)
from src.apps.expense_tracker.utils.report_generator import generate_report

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


@router.get("/report/")
def generate_excel_report(
    start_date: Optional[date] = None,
    end_date: Optional[date] = date.today(),
    db: Session = Depends(get_db),
):
    articles = crud.get_articles(db, start_date, end_date)

    if not articles:
        raise HTTPException(status_code=404, detail="No expenses found for the given period")

    report_path = generate_report(articles)

    return FileResponse(
        report_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=report_path.name
    )
