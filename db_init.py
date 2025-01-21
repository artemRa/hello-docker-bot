import sqlite3

db_name = "data/hello-docker-log.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS actions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    );
""")
conn.commit()
conn.close()
