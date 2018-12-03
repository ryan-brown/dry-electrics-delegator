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
    cursor.execute("""select id, username, percentage, charging, max(updated_at) from updates group by username""")

    return cursor.fetchall()

def get_user_data(username):
  with sqlite3.connect("database.db") as conn:
    cursor= conn.cursor()
    cursor.execute("""SELECT * FROM updates where username = '{}' """.format(username))

    return cursor.fetchall()

def select_everything():
  with sqlite3.connect("database.db") as conn:
    cursor= conn.cursor()
    cursor.execute("""select * from updates""")

    return cursor.fetchall()
