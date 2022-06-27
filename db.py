from multiprocessing import connection
import sqlite3
from unicodedata import name
connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()
# cursor.execute("CREATE TABLE User ( name TEXT,age INT;)")
# cursor.execute("INSERT INTO User VALUES(Amaka,23)")
# cursor.execute("SELECT * FROM User")
# print(cursor.fetchone())
# cursor.executemany("")
# cursor.executescript("")
name = "uche"
age=45
cursor.execute(f"INSERT INTO User VALUES(?,?)",(name,age))
connection.commit()
connection.close()

from dotenv import load_dotenv
