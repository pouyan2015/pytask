import sys
from PySide6.QtWidgets import QApplication
from database.migrations import initialize
from themes.theme_manager import load_theme
from ui.main_window import MainWindow
from app.config import get_setting

def main():
    initialize()
    app = QApplication(sys.argv)
    
    # Load saved theme (defaults to dark)
    saved_theme = get_setting("theme", "dark")
    app.setStyleSheet(load_theme(saved_theme))

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
