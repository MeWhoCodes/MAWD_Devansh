import sqlite3

conn = sqlite3.connect("Students.db")

vikram = ("Vikram","BCA","Udaipur",67)

cursor = conn.cursor()

cursor.execute("insert into Students (name,course,city,marks)",vikram)
