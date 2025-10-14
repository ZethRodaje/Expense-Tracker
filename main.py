import sys
from PyQt6.QtWidgets import QApplication
from core import db
from shell.main_window import MainWindow
from pathlib import Path

# Load QSS theme if available.
def load_stylesheet(app):
    qss = Path("core/styles.qss")
    if qss.exists():
        with open(qss, "r", encoding="utf-8") as f: #encoding utf-8 to ccontain special characters
            app.setStyleSheet(f.read())

# Starting the program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    db.init_db()
    load_stylesheet(app)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())