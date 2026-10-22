from pathlib import Path
import os, sys
import sqlite3

APP_NAME = "PyTasks"
APP_AUTHOR = "Arasaka"

def app_data_dir() -> Path:
    if sys.platform == "win32":
        base = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
    elif sys.platform == "darwin":
        base = Path.home() / "Library" / "Application Support"
    else:
        base = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))
    p = base / APP_NAME
    p.mkdir(parents=True, exist_ok=True)
    return p

DATA_DIR = app_data_dir()
DB_PATH = DATA_DIR / "pytasks.db"
BACKUP_DIR = DATA_DIR / "backups"
BACKUP_DIR.mkdir(parents=True, exist_ok=True)

def get_setting(key: str, default: str = "") -> str:
    try:
        conn = sqlite3.connect(DB_PATH)
        row = conn.execute("SELECT value FROM settings WHERE key=?", (key,)).fetchone()
        conn.close()
        return row[0] if row else default
    except Exception:
        return default

def set_setting(key: str, value: str):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO settings(key, value) VALUES(?, ?) ON CONFLICT(key) DO UPDATE SET value=excluded.value", (key, value))
    conn.commit()
    conn.close()
