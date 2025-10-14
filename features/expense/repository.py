from core.db import run_query
from features.expense.models import Expense

def all_expenses():
    rows = run_query("SELECT id, title, amount, date, category, description FROM expenses ORDER BY date DESC, id DESC")
    return [Expense(*row) for row in rows]

def get_expense(expense_id: int):
    rows = run_query("SELECT id, title, amount, date, category, description FROM expenses WHERE id=?", (expense_id,))
    return Expense(*rows[0]) if rows else None

def add_expense(exp: Expense):
    run_query("INSERT INTO expenses (title, amount, date, category, description) VALUES (?, ?, ?, ?, ?)",
    (exp.title, exp.amount, exp.date, exp.category, exp.description),)

def update_expense(exp: Expense):
    run_query("UPDATE expenses SET title=?, amount=?, date=?, category=?, description=? WHERE id=?",
    (exp.title, exp.amount, exp.date, exp.category, exp.description, exp.id),)

def delete_expense(expense_id: int):
    run_query("DELETE FROM expenses WHERE id=?", (expense_id,))