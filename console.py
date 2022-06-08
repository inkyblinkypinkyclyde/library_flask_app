import pdb
from models.author import Author
from models.book import Book

from repositories import author_repository, book_repository

author1 = Author("J. R. R Tolkien")
author_repository.save(author1)

book1 = Book("Lord of the Rings", author1, "Rings")
book_repository.save(book1)
book2 = Book("The Hobbit", author1, "Hobbits")
book_repository.save(book2)

pdb.set_trace()