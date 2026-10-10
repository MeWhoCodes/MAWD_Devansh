# Section B, question B1
import sqlite3

conn = sqlite3.connect("Students.db")

conn.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                course TEXT,
                city TEXT,
                marks INTEGER
            )
    """)

cursor = conn.cursor()

bsc_students = [
    ("Aman","BSc","Jaipur",78),
    ("Priya","BCA","Pali",88),
    ("Rahul","Bsc","Jodhpur",45),
    ("Sneha","BSc","Pali",92),
    ("Karan","BCA","Jaipur",30)
]

cursor.executemany("insert into Students (name,course,city,marks) values (?,?,?,?)", bsc_students)

conn.commit()

conn.close()