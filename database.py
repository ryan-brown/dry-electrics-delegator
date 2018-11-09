import sqlite3

def insert_update(username, percentage, charging, updated_at):
  with sqlite3.connect("database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO updates (username, percentage, charging, updated_at) VALUES (?, ?, ?, ?)",
      (username, percentage, charging, updated_at))
    conn.commit()

def select_all():
  with sqlite3.connect("database.db") as conn:
    cursor= conn.cursor()
    cursor.execute("""SELECT * FROM updates temp
      WHERE updated_at = (SELECT MAX(updated_at) FROM updates WHERE updates.username = temp.username)""")

    return cursor.fetchall()