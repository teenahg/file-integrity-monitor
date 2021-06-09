import sqlite3

conn = sqlite3.connect('fim.sqlite3')
c = conn.cursor()

def get_files():
  with conn:
    result = c.execute("SELECT * FROM filemanager_file")
    print(result)
    return c.fetchall()

get_files()