import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('progress.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS activity
                 (id INTEGER PRIMARY KEY,
                  feature TEXT,
                  timestamp TEXT,
                  details TEXT)''')
    conn.commit()
    conn.close()

def log_activity(feature, details=""):
    conn = sqlite3.connect('progress.db')
    c = conn.cursor()
    c.execute("INSERT INTO activity (feature, timestamp, details) VALUES (?, ?, ?)",
              (feature, datetime.now().strftime("%Y-%m-%d %H:%M"), details))
    conn.commit()
    conn.close()

def get_stats():
    conn = sqlite3.connect('progress.db')
    c = conn.cursor()
    c.execute("SELECT feature, COUNT(*) as count FROM activity GROUP BY feature")
    stats = c.fetchall()
    c.execute("SELECT * FROM activity ORDER BY timestamp DESC LIMIT 10")
    recent = c.fetchall()
    conn.close()
    return stats, recent 