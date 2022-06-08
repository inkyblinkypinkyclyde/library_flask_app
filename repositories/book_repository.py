from db.run_sql import run_sql

from models.book import Book
import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, author_id, blurb, read) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.blurb, book.read]
    results = run_sql(sql, values)
    id = results[0]['id']
#######wtf is with this this thing???????
    book.id = id
    return book

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    for row in results:
        author = author_repository.select(row['author_id'])
        task = Book(row['title'], author, row['blurb'], row['read'], row['id'] )
        books.append(task)
    return books

def select(id):
    book = None
    sql = 'SELECT * FROM books WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)
    if result is not None:
        author = author_repository.select(result['id'])
        book = Book(result['title'], author, result['blurb'], result['read'], result['id'])
    return book

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(book):
    sql = "UPDATE books SET (title, author, blurb, read) = (%s, %s, %s, %s) WHERE id = %s"
    values = [book.description, book.user.id, book.blurb, book.read, book.id]
    run_sql(sql, values)