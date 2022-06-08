from flask import Flask, redirect, render_template, request
from repositories import book_repository, author_repository
from models.book import Book

from flask import Blueprint

books_blueprint = Blueprint("tasks", __name__)

# INDEX
# GET '/tasks'
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all() # NEW
    return render_template("books/index.html", all_books = books)