from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QPainter, QColor, QFont
from PySide6.QtCore import Qt
from database.repositories import task_repo

class BarChart(QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data = data
        self.setMinimumHeight(300)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        if not self.data: return
        
        width = self.width()
        height = self.height()
        bar_width = width // (len(self.data) * 2)
        max_val = max(self.data.values()) or 1
        
        for i, (label, val) in enumerate(self.data.items()):
            x = i * (bar_width * 2) + bar_width
            h = (val / max_val) * (height - 40)
            y = height - h - 20
            
            painter.setBrush(QColor("#89b4fa"))
            painter.setPen(Qt.NoPen)
            painter.drawRect(x, int(y), bar_width, int(h))
            
            painter.setPen(QColor("#cdd6f4"))
            painter.setFont(QFont("Segoe UI", 10))
            painter.drawText(x, height - 5, label)
            painter.drawText(x, int(y) - 5, str(val))

class AnalyticsView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(14)
        
        title = QLabel("ANALYTICS"); title.setObjectName("PageTitle")
        self.layout.addWidget(title)
        self.chart_container = QVBoxLayout()
        self.layout.addLayout(self.chart_container)
        self.layout.addStretch()

    def refresh(self):
        while self.chart_container.count():
            item = self.chart_container.takeAt(0)
            if item.widget(): item.widget().deleteLater()

        c = task_repo.counts()
        data = {"Active": c["active"], "Completed": c["completed"], "Overdue": c["overdue"], "Archived": c["archived"]}
        self.chart_container.addWidget(BarChart(data))
