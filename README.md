Proponent(s)
------------
Rodaje, Zeth Gabriel C. – BSCS

Project Overview
----------------
The Expense Tracker is a desktop application that allows users to record, view, and manage daily expenses.
It helps users monitor spending habits and maintain budget awareness.
The system was developed in Python using PyQt6 for the GUI and SQLite for the database.

Features
--------
• Add, edit, and delete expense records (CRUD)

• View all transactions in a sortable table

• Auto-load data on startup

• Double-click a record to edit

• Optional styles.qss for custom design

• SQLite database storage

Code Design and Structure
-------------------------
• main.py – main entry point of the program

• core/ – contains the database connection and stylesheet

• features/expenses – includes models, repository, service, and view files

• shell/ – contains the main window for the interface


The code is organized into separate modules for clarity, following a simple MVC-like structure.
Each part handles a specific responsibility to make the program easy to maintain.

Screenshots
-----------

• Main window with table
• Example of adding or editing a record

How to Run the Program
----------------------
1. Make sure Python 3.9+ is installed.
2. Install dependencies:
   pip install PyQt6
3. Open the project folder in your terminal or IDE.
4. Run the app using:
   python main.py
