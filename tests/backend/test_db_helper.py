from backend import db_helper

def test_fetch_expenses_for_date():
    expense=db_helper.fetch_expenses_for_date("2024-08-15")
    assert len(expense)==1
    assert expense[0]['amount']==10.0
    assert expense[0]['category'] =="Shopping"
    assert expense[0]['notes'] == "Bought potatoes"

def test_fetch_expenses_for_date_invalid_date():
    expense=db_helper.fetch_expenses_for_date("1999-08-15")
    assert len(expense)==0

def test_fetch_expense_summary():
    expense=db_helper.fetch_expense_summary("9999-08-15","2024-08-13")
    assert len(expense)==0

