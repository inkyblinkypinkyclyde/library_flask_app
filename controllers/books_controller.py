from flask import Flask, redirect, render_template, request
from repositories import book_repository, author_repository
from models.book import Book

from flask import Blueprint

books_blueprint = Blueprint("tasks", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)



#new
#get
@books_blueprint.route('/books/new', methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template('/books/new.html', all_authors = authors)

#create
#post
@books_blueprint.route('/books/', methods=['POST'])
def create_book():
    title = request.form['title'] 
    author_id = request.form['author_id']
    blurb = request.form['blurb']
    read = request.form['read']
    author = author_repository.select(author_id)
    book = Book(title, author, blurb, read)
    book_repository.save(book)
    return redirect('/books')


#show
#get
@books_blueprint.route('/book/<id>', methods=['GET'])
def show_book(id):
    book = book_repository.select(id)
    return render_template('books/<id>/show.html', book = book)

#edit
#get

#update
#put

#delete
#delete