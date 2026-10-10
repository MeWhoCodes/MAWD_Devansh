from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def get_db():
    conn = sqlite3.connect("shop.db")
    conn.row_factory = sqlite3.Row  # This lets us access columns by name
    return conn


conn = get_db()
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        price REAL,
        code TEXT
    )
""")
conn.commit()
conn.close()

# Pydantic model of a Book
class Book(BaseModel):
    title: str
    author: str
    price: float
    code: str

@app.post("/books", status_code=201)
def add_book(book: Book):
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO books (title, author, price, code) VALUES (?, ?, ?, ?)",
        (book.title, book.author, book.price, book.code)
    )
    conn.commit()
    book_id = cursor.lastrowid  # Get the ID of the newly added book
    conn.close()
    
    return {
        "id": book_id,
        "title": book.title,
        "author": book.author,
        "price": book.price,
        "code": book.code
    }


@app.get("/books")
def get_all_books():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    
    books_list = []
    for row in rows:
        books_list.append({
            "id": row["id"],
            "title": row["title"],
            "author": row["author"],
            "price": row["price"],
            "code": row["code"]
        })
    return books_list

@app.get("/books/{book_id}")
def get_single_book(book_id: int):
    conn = get_db()
    cursor = conn.cursor()
    
   
    cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row is None:
        raise HTTPException(status_code=404, detail="Book not found")
        
    return {
        "id": row["id"],
        "title": row["title"],
        "author": row["author"],
        "price": row["price"],
        "code": row["code"]
    }


@app.put("/book/{book_id}")
def update_book(book_id: int, book: Book):
    conn = get_db()
    cursor = conn.cursor()
    
  
    cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    row = cursor.fetchone()
    if row is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")
        
   
    cursor.execute(
        "UPDATE books SET title = ?, author = ?, price = ?, code = ? WHERE id = ?",
        (book.title, book.author, book.price, book.code, book_id)
    )
    conn.commit()
    conn.close()
    
    return {
        "id": book_id,
        "title": book.title,
        "author": book.author,
        "price": book.price,
        "code": book.code
    }


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    conn = get_db()
    cursor = conn.cursor()
    


    
    cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    row = cursor.fetchone()
    if row is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")
        
    
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    
    return {"message": f"Book with id {book_id} was deleted successfully."}