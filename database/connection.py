import sqlite3
from contextlib import contextmanager
from app.config import DB_PATH

_conn = None

def get_connection() -> sqlite3.Connection:
    global _conn
    if _conn is None:
        _conn = sqlite3.connect(DB_PATH)
        _conn.row_factory = sqlite3.Row
        _conn.execute("PRAGMA foreign_keys = ON;")
        _conn.execute("PRAGMA journal_mode = WAL;")
        _conn.execute("PRAGMA synchronous = NORMAL;")
    return _conn

@contextmanager
def transaction():
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise

def close_connection():
    global _conn
    if _conn is not None:
        _conn.close()
        _conn = None
