from PyQt6.QtWidgets import QMainWindow
from features.expense.view import ExpenseView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expense Tracker")
        self.resize(900, 520)
        self.setCentralWidget(ExpenseView())