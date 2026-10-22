from PySide6.QtWidgets import QWidget, QVBoxLayout, QCalendarWidget, QLabel
from PySide6.QtCore import QDate
from PySide6.QtGui import QTextCharFormat, QColor
from database.connection import get_connection

class CalendarView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(14)
        
        title = QLabel("CALENDAR"); title.setObjectName("PageTitle")
        layout.addWidget(title)

        self.cal = QCalendarWidget()
        self.cal.setGridVisible(True)
        self.cal.setStyleSheet("""
            QCalendarWidget QWidget { background-color: #1e1e2e; color: #cdd6f4; }
            QCalendarWidget QAbstractItemView { selection-background-color: #89b4fa; selection-color: #11111b; }
        """)
        layout.addWidget(self.cal, 1)
        
        self.info = QLabel("Select a date to view tasks.")
        self.info.setStyleSheet("font-size: 15px; color: #a6adc8;")
        layout.addWidget(self.info)
        
        self.cal.selectionChanged.connect(self.on_date_selected)

    def on_date_selected(self):
        selected = self.cal.selectedDate().toString("yyyy-MM-dd")
        conn = get_connection()
        rows = conn.execute("SELECT title FROM tasks WHERE date(due_at) = ? AND deleted=0", (selected,)).fetchall()
        if not rows:
            self.info.setText(f"No tasks due on {selected}.")
        else:
            tasks = "\n".join([f"- {r['title']}" for r in rows])
            self.info.setText(f"Tasks due on {selected}:\n{tasks}")

    def refresh(self):
        # Highlight days with tasks
        self.cal.setDateTextFormat(QDate(), QTextCharFormat())
        conn = get_connection()
        rows = conn.execute("SELECT due_at FROM tasks WHERE due_at IS NOT NULL AND deleted=0").fetchall()
        fmt = QTextCharFormat()
        fmt.setBackground(QColor("#89b4fa"))
        fmt.setForeground(QColor("#11111b"))
        for r in rows:
            d = QDate.fromString(r["due_at"][:10], "yyyy-MM-dd")
            if d.isValid():
                self.cal.setDateTextFormat(d, fmt)
