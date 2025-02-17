import mysql.connector
from contextlib import contextmanager
from setup_Logger import set_up_logegr

logger=set_up_logegr('db_helper')



@contextmanager
def get_db_cursor(commit=False):
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root",
            database="expense_manager"
        )
        cursor=connection.cursor(dictionary=True)
        yield cursor
        if commit:
            connection.commit()
        cursor.close()
        connection.close()

def fetch_all_records():
    logger.info(f"fetch_all_records")
    with get_db_cursor() as cursor:
        cursor.execute("select * from expenses;")
        expenses=cursor.fetchall()
        for expense in expenses:
            print(expense)

def fetch_all_records_by_month(month:int):
    logger.info(f"fetch_all_records by month")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT category,sum(amount) as total FROM expenses WHERE MONTH(expense_date) = %s AND YEAR(expense_date) = 2024 group by category",(month,))
        expenses=cursor.fetchall()
        return expenses

def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date with date:{expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("select * from expenses where expense_date=%s",(expense_date,))
        expenses=cursor.fetchall()
        return expenses

def insert_expenses(expense_date,amount,category,notes):
    logger.info(f"insert_expenses with date:{expense_date},amount:{amount},category:{category},notes:{notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("insert INTO expenses (expense_date,amount,category,notes) values(%s,%s,%s,%s)",
                       (expense_date,amount,category,notes))

def fetch_expense_summary(start_date,end_date):
    with get_db_cursor() as cursor:
        logger.info(f"fetch_expense_summary with start date:{start_date} end_date{end_date}")
        cursor.execute("SELECT category,sum(amount) as total FROM expenses where expense_date between %s and %s group by category",
                       (start_date,end_date))
        records=cursor.fetchall()
        return records

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date with date:{expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("delete from expenses where expense_date=%s",(expense_date,))


if __name__=="__main__":
    expense = fetch_all_records_by_month(9)
    for exp in expense:
        print(exp)

