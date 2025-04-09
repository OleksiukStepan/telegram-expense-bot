from fastapi import FastAPI
from src.apps.expense_tracker import models
from src.apps.expense_tracker.database import engine
from src.apps.expense_tracker.api import router as expense_router

app = FastAPI(
    title="Expense Tracker API",
    description="API for tracking personal expenses",
    version="1.0.0"
)

models.Base.metadata.create_all(bind=engine)

app.include_router(expense_router, prefix="/expenses", tags=["Expenses"])
