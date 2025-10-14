from . import repository
from features.expense.models import Expense

def list_expenses():
    return repository.all_expenses()

def create_expense(title, amount, date, category, description):
    exp = Expense(None, title, amount, date, category, description)
    repository.add_expense(exp)




def edit_expense(expense_id, title, amount, date, category, description):
    exp = Expense(expense_id, title, amount, date, category, description)
    repository.update_expense(exp)




def remove_expense(expense_id):
    repository.delete_expense(expense_id)




def get_expense(expense_id):
    return repository.get_expense(expense_id)