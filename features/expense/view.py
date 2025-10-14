from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QDate
from datetime import datetime
from features.expense import service


# Expense View class that handles all User Interface and events.
class ExpenseView(QWidget):
    def __init__(self):
        super().__init__()
        self.editing_id = None
        self.setup_ui()

    def showEvent(self, event):
        super().showEvent(event)
        self.load_data()

    # Setup layout and widgets
    def setup_ui(self):
        main_layout = QHBoxLayout(self)

        # Left side form
        left = QVBoxLayout()
        form = QFormLayout()
        self.input_title = QLineEdit()
        self.input_amount = QLineEdit()
        self.input_date = QDateEdit()
        self.input_date.setCalendarPopup(True)
        self.input_date.setDate(QDate.currentDate())
        self.input_category = QComboBox()
        self.input_category.setEditable(True)
        self.input_category.addItems(["Food", "Transport", "Bills", "Shopping", "Other"])
        self.input_description = QTextEdit()


        form.addRow("Title:", self.input_title)
        form.addRow("Amount:", self.input_amount)
        form.addRow("Date:", self.input_date)
        form.addRow("Category:", self.input_category)
        form.addRow("Description:", self.input_description)


        left.addLayout(form)


        # buttons
        btns = QHBoxLayout()
        self.btn_add_save = QPushButton("Add")
        self.btn_add_save.clicked.connect(self.on_add_or_update)
        self.btn_clear = QPushButton("Clear")
        self.btn_clear.clicked.connect(self.clear_form)
        self.btn_delete = QPushButton("Delete")
        self.btn_delete.clicked.connect(self.on_delete)
        btns.addWidget(self.btn_add_save)
        btns.addWidget(self.btn_clear)
        btns.addWidget(self.btn_delete)
        
        left.addLayout(btns)
        
        left.addWidget(QLabel("Double-click a row to edit."))
        main_layout.addLayout(left, 1)


        # Right side table
        right = QVBoxLayout()
        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels(["ID", "Title", "Amount", "Date", "Category", "Description"])
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.cellDoubleClicked.connect(self.on_row_double_click)


        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)


        right.addWidget(self.table)
        main_layout.addLayout(right, 2)
    
    # Load all data into table.
    def load_data(self):
        self.table.setRowCount(0)
        for exp in service.list_expenses():
            r = self.table.rowCount()
            self.table.insertRow(r)
            self.table.setItem(r, 0, QTableWidgetItem(str(exp.id)))
            self.table.setItem(r, 1, QTableWidgetItem(exp.title))
            self.table.setItem(r, 2, QTableWidgetItem(str(exp.amount)))
            self.table.setItem(r, 3, QTableWidgetItem(exp.date))
            self.table.setItem(r, 4, QTableWidgetItem(exp.category))
            self.table.setItem(r, 5, QTableWidgetItem(exp.description))
    
    # Clear form fields.
    def clear_form(self):
        self.input_title.clear()
        self.input_amount.clear()
        self.input_date.setDate(QDate.currentDate())
        self.input_category.setCurrentIndex(0)
        self.input_description.clear()
        self.editing_id = None
        self.btn_add_save.setText("Add")

    # Add or update record.
    def on_add_or_update(self):
        title = self.input_title.text().strip()
        try:
            amount = float(self.input_amount.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Validation", "Amount must be numeric")
            return
        date_str = self.input_date.date().toString("yyyy-MM-dd")
        category = self.input_category.currentText()
        description = self.input_description.toPlainText()


        if self.editing_id:
            service.edit_expense(self.editing_id, title, amount, date_str, category, description)
        else:
            service.create_expense(title, amount, date_str, category, description)
        self.load_data()
        self.clear_form()

    # Delete selected record.
    def on_delete(self):
        sel = self.table.selectedItems()
        if not sel:
            return
        row = sel[0].row()
        exp_id = int(self.table.item(row, 0).text())
        service.remove_expense(exp_id)
        self.load_data()

    # Load selected record into form for editing.
    def on_row_double_click(self, row, col):
        exp_id = int(self.table.item(row, 0).text())
        exp = service.get_expense(exp_id)
        if not exp:
            return
        self.editing_id = exp.id
        self.input_title.setText(exp.title)
        self.input_amount.setText(str(exp.amount))
        try:
            dt = datetime.strptime(exp.date, "%Y-%m-%d")
            self.input_date.setDate(QDate(dt.year, dt.month, dt.day))
        except:
            pass
        idx = self.input_category.findText(exp.category)
        if idx == -1:
            self.input_category.addItem(exp.category)
            idx = self.input_category.findText(exp.category)
        self.input_category.setCurrentIndex(idx)
        self.input_description.setText(exp.description)
        self.btn_add_save.setText("Save Changes") 