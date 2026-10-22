from database.connection import get_connection
from database.schema import SCHEMA_SQL, SCHEMA_VERSION

def initialize():
    conn = get_connection()
    conn.executescript(SCHEMA_SQL)
    row = conn.execute("SELECT value FROM schema_meta WHERE key='version'").fetchone()
    current_version = int(row["value"]) if row else 0
    if current_version < 2:
        try: conn.execute("ALTER TABLE tasks ADD COLUMN status INTEGER NOT NULL DEFAULT 0")
        except Exception: pass
        conn.execute("UPDATE schema_meta SET value=? WHERE key='version'", (str(SCHEMA_VERSION),))
    conn.commit()
