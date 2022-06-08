from db.run_sql import run_sql

from models.book import Book

def save(book):
    sql = "INSERT INTO books (title, author_id, blurb, read) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.blurb, book.read]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        book = artist_repository.select(row['user_id'])
        task = Book(row['description'], user, row['duration'], row['completed'], row['id'] )
        tasks.append(task)
    return tasks