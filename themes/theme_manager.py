PREMIUM_DARK_QSS = """
QWidget {
    background-color: transparent;
    color: #cdd6f4;
    font-family: "Segoe UI", "Inter", sans-serif;
    font-size: 14px;
}
#MainContainer {
    background-color: #11111b;
    border-radius: 20px;
    border: 1px solid #313244;
}
#Sidebar {
    background-color: #181825;
    border-top-left-radius: 20px;
    border-bottom-left-radius: 20px;
    border-right: 1px solid #313244;
}
#Sidebar QPushButton {
    background-color: transparent;
    color: #a6adc8;
    border: none;
    border-radius: 10px;
    text-align: left;
    padding: 12px 16px;
    margin: 4px 12px;
    font-weight: 600;
    letter-spacing: 0.5px;
    border-left: 3px solid transparent;
}
#Sidebar QPushButton:hover {
    background-color: #1e1e2e;
    color: #cdd6f4;
}
#Sidebar QPushButton:checked {
    background-color: #1e1e2e;
    color: #cdd6f4;
    border-left: 3px solid #f38ba8;
}
#Hamburger {
    background: transparent;
    color: #cdd6f4;
    border: none;
    font-size: 16px;
    font-weight: 900;
    padding: 18px 20px;
    text-align: left;
    letter-spacing: 2px;
}
#Hamburger:hover { color: #f38ba8; }
#PageTitle {
    color: #cdd6f4;
    font-size: 26px;
    font-weight: 900;
    letter-spacing: 1px;
    background: transparent;
}
QPushButton#PrimaryBtn {
    background-color: #58cc02;
    color: #ffffff;
    border: none;
    border-radius: 12px;
    border-bottom: 4px solid #46a302;
    padding: 10px 20px;
    font-weight: 800;
    letter-spacing: 1px;
}
QPushButton#PrimaryBtn:hover { background-color: #61e002; }
QPushButton#PrimaryBtn:pressed {
    background-color: #46a302;
    border-bottom: 0px solid #46a302;
    padding-top: 14px;
    padding-bottom: 6px;
}
QPushButton#GhostBtn {
    background-color: #1cb0f6;
    color: #ffffff;
    border: none;
    border-radius: 12px;
    border-bottom: 4px solid #1899d6;
    padding: 10px 20px;
    font-weight: 800;
    letter-spacing: 1px;
}
QPushButton#GhostBtn:hover { background-color: #3ec0ff; }
QPushButton#GhostBtn:pressed {
    background-color: #1899d6;
    border-bottom: 0px solid #1899d6;
    padding-top: 14px;
    padding-bottom: 6px;
}
QPushButton#CloseBtn {
    background-color: #ff4b4b;
    color: #ffffff;
    border: none;
    border-radius: 12px;
    border-bottom: 4px solid #cc3b3b;
    padding: 10px 14px;
    margin: 8px;
    font-weight: 800;
    text-align: left;
}
QPushButton#CloseBtn:hover { background-color: #ff5f5f; }
QPushButton#CloseBtn:pressed {
    background-color: #cc3b3b;
    border-bottom: 0px solid #cc3b3b;
    padding-top: 14px;
    padding-bottom: 6px;
}
QLineEdit {
    background-color: #313244;
    color: #cdd6f4;
    border: 2px solid #45475a;
    border-radius: 14px;
    padding: 12px 16px;
    font-size: 15px;
}
QLineEdit:focus { border: 2px solid #89b4fa; }
QListWidget {
    background-color: #181825;
    border: 2px solid #313244;
    border-radius: 16px;
    padding: 8px;
    outline: none;
}
QListWidget::item {
    background-color: #313244;
    border-radius: 12px;
    margin-bottom: 6px;
    border-bottom: 2px solid #1e1e2e;
}
QListWidget::item:selected {
    background-color: #45475a;
    border-left: 4px solid #89b4fa;
}
QScrollBar:vertical {
    background: transparent; width: 8px; margin: 0;
}
QScrollBar::handle:vertical {
    background: #45475a; border-radius: 4px; min-height: 24px;
}
QScrollBar::handle:vertical:hover { background: #585b70; }
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
#StatCard {
    background-color: #313244;
    border-radius: 16px;
    border-bottom: 4px solid #1e1e2e;
}
#StatValue { color: #cdd6f4; font-size: 28px; font-weight: 900; background: transparent; }
#StatLabel { color: #a6adc8; font-size: 12px; font-weight: 700; background: transparent; }
"""

PREMIUM_LIGHT_QSS = """
QWidget {
    background-color: transparent;
    color: #4c4f69;
    font-family: "Segoe UI", "Inter", sans-serif;
    font-size: 14px;
}
#MainContainer {
    background-color: #eff1f5;
    border-radius: 20px;
    border: 1px solid #ccd0da;
}
#Sidebar {
    background-color: #e6e9ef;
    border-top-left-radius: 20px;
    border-bottom-left-radius: 20px;
    border-right: 1px solid #ccd0da;
}
#Sidebar QPushButton {
    background-color: transparent;
    color: #6c6f85;
    border: none;
    border-radius: 10px;
    text-align: left;
    padding: 12px 16px;
    margin: 4px 12px;
    font-weight: 600;
    letter-spacing: 0.5px;
    border-left: 3px solid transparent;
}
#Sidebar QPushButton:hover {
    background-color: #dce0e8;
    color: #4c4f69;
}
#Sidebar QPushButton:checked {
    background-color: #dce0e8;
    color: #4c4f69;
    border-left: 3px solid #d20f39;
}
#Hamburger {
    background: transparent;
    color: #4c4f69;
    border: none;
    font-size: 16px;
    font-weight: 900;
    padding: 18px 20px;
    text-align: left;
    letter-spacing: 2px;
}
#Hamburger:hover { color: #d20f39; }
#PageTitle {
    color: #4c4f69;
    font-size: 26px;
    font-weight: 900;
    letter-spacing: 1px;
    background: transparent;
}
QPushButton#PrimaryBtn {
    background-color: #1e66f5;
    color: #ffffff;
    border: none;
    border-radius: 10px;
    border-bottom: 3px solid #124bbd;
    padding: 10px 24px;
    font-weight: 900;
    letter-spacing: 1px;
}
QPushButton#PrimaryBtn:hover { background-color: #4a85f7; }
QPushButton#PrimaryBtn:pressed {
    background-color: #124bbd;
    border-bottom: 0px solid #124bbd;
    padding-top: 13px;
    padding-bottom: 7px;
}
QPushButton#GhostBtn {
    background-color: #ccd0da;
    color: #4c4f69;
    border: none;
    border-radius: 10px;
    border-bottom: 3px solid #bcc0cc;
    padding: 10px 24px;
    font-weight: 800;
    letter-spacing: 1px;
}
QPushButton#GhostBtn:hover { background-color: #bcc0cc; }
QPushButton#GhostBtn:pressed {
    background-color: #bcc0cc;
    border-bottom: 0px solid #bcc0cc;
    padding-top: 13px;
    padding-bottom: 7px;
}
QPushButton#CloseBtn {
    background-color: #d20f39;
    color: #ffffff;
    border: none;
    border-radius: 10px;
    border-bottom: 3px solid #9c0627;
    padding: 10px 16px;
    margin: 12px;
    font-weight: 900;
    text-align: left;
}
QPushButton#CloseBtn:hover { background-color: #e64553; }
QPushButton#CloseBtn:pressed {
    background-color: #9c0627;
    border-bottom: 0px solid #9c0627;
    padding-top: 13px;
    padding-bottom: 7px;
}
QLineEdit {
    background-color: #ffffff;
    color: #4c4f69;
    border: 1px solid #ccd0da;
    border-radius: 10px;
    padding: 12px 16px;
    font-size: 15px;
}
QLineEdit:focus { border: 1px solid #1e66f5; }
QListWidget {
    background-color: #e6e9ef;
    border: 1px solid #ccd0da;
    border-radius: 12px;
    padding: 8px;
    outline: none;
}
QListWidget::item {
    background-color: #ffffff;
    border-radius: 8px;
    margin-bottom: 6px;
    border-bottom: 2px solid #eff1f5;
}
QListWidget::item:selected {
    background-color: #dce0e8;
    border-left: 3px solid #1e66f5;
}
QScrollBar:vertical {
    background: transparent; width: 8px; margin: 0;
}
QScrollBar::handle:vertical {
    background: #ccd0da; border-radius: 4px; min-height: 24px;
}
QScrollBar::handle:vertical:hover { background: #bcc0cc; }
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
#StatCard {
    background-color: #e6e9ef;
    border-radius: 12px;
    border: 1px solid #ccd0da;
    border-top: 2px solid #1e66f5;
}
#StatValue { color: #4c4f69; font-size: 32px; font-weight: 900; background: transparent; }
#StatLabel { color: #6c6f85; font-size: 11px; font-weight: 800; letter-spacing: 1px; background: transparent; }
"""

def load_theme(theme_name):
    if theme_name == "dark":
        return PREMIUM_DARK_QSS
    return PREMIUM_LIGHT_QSS
