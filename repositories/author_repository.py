from db.run_sql import run_sql

from models.author import Author
import repositories.author_repository as author_repository


def save(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def delete(id):
    sql = "DELETE FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)