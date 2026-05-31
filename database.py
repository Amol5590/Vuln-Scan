
import sqlite3

DB="scan_history.db"

def init_db():
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS scans(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        result TEXT
    )''')
    conn.commit()
    conn.close()

def save_scan(url,result):
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute("INSERT INTO scans(url,result) VALUES(?,?)",(url,result))
    conn.commit()
    conn.close()

def get_scans():
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute("SELECT url,result FROM scans ORDER BY id DESC")
    data=c.fetchall()
    conn.close()
    return data
