from fastapi import FastAPI
from datetime import date
from typing import List
from pydantic import BaseModel
import db_helper
import logging

app=FastAPI()

class Expense(BaseModel):
    amount:float
    category:str
    notes:str

class DateRange(BaseModel):
    start_date:date
    end_date:date


@app.get("/expenses/{expense_date}",response_model=List[Expense])
def get_expenses(expense_date:date):
    expenses=db_helper.fetch_expenses_for_date(expense_date)
    return expenses


logging.basicConfig(level=logging.INFO)


@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expenses(expense_date, expense.amount, expense.category, expense.notes)

    return {"message": "Expense added successfully"}

@app.post("/analytics/")
def analytics_summary(date_range:DateRange):
    data=db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)
    total=sum([row['total'] for row in data])
    breakdown={}
    for row in data:
        percentage=(row['total']/total)*100
        breakdown[row['category']]={
           "total":row['total'],
            "percentage":percentage
        }


    return breakdown

@app.get("/expenses/by_month/{expense_month}")
def get_expenses(expense_month:int):
    data=db_helper.fetch_all_records_by_month(expense_month)
    total=sum([row['total'] for row in data])
    breakdown={}
    for row in data:
        percentage=(row['total']/total)*100
        breakdown[row['category']]={
           "total":row['total'],
            "percentage":percentage
        }


    return breakdown


logging.basicConfig(level=logging.INFO)


