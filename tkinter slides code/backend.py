import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

connect()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    c=conn.cursor()
    c.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    c=conn.cursor()
    c.execute("SELECT * FROM book")
    rows=c.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    c=conn.cursor()
    c.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows=c.fetchall()
    conn.close()

def delete(id):
    conn=sqlite3.connect("books.db")
    c=conn.cursor()
    c.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

connect()
insert("The Sun","John Smith",1918,913123132)
delete(3)
print(view())
print(search(author="John Smith"))

