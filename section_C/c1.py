import sqlite3

conn = sqlite3.connect("library.db")

conn.execute("""
            CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT,
                price REAL                
            )
    """)
conn.commit()
conn.close()



conn = sqlite3.connect("library.db")
cursor = conn.cursor()

bunch_of_books = [
    ("Python Basics","Rao",250),
    ("SQL Guide","Mehta",180),
    ("Web Dev","Khan",400)
]

cursor.executemany("insert into library (title,author,price) values (?,?,?)", bunch_of_books)


conn.commit()
conn.close()






conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("update price to 198 from library where id=2")
conn.commit()
conn.close




conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("delete from library where price<200")
conn.commit()
conn.close




conn = sqlite3.connect("library.db")
conn.execute("select * from library")



# will return the following:
# Python Baics   Rao   250
# Web Dev        Khan  400