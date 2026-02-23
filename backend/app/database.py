from pathlib import Path
import sqlite3

def init_db():
  con = sqlite3.connect(Path(__file__).parent.parent/"data"/"learnout.db")
  cur = con.cursor()

  cur.execute("""
    CREATE TABLE IF NOT EXISTS sessions (
      session_id TEXT PRIMARY KEY, 
      topic TEXT, 
      created_at TEXT
    )
  """)
  
  cur.execute("""
    CREATE TABLE IF NOT EXISTS messages (
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      session_id TEXT, 
      role TEXT, 
      content TEXT, 
      created_at TEXT
    )
  """)
  
  con.commit()
  con.close()