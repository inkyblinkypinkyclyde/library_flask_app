import pdb
from models.author import Author
from models.book import Book

from repositories import author_repository, book_repository

author1 = Author("J. R. R Tolkien")
author_repository.save(author1)
author2 = Author("Douglas Adams")
author_repository.save(author2)

book1 = Book("Lord of the Rings", author1, "Rings and stuff")
book_repository.save(book1)
book2 = Book("The Hobbit", author1, "Dragons and stuff")
book_repository.save(book2)
book3 = Book("The Hitchhikers Guide to the Galaxy", author2, "Space and stuff")
book_repository.save(book3)
book4 = Book("The Restaurant at the edge of the Universe", author2, "Space and stuff too")
book_repository.save(book4)

pdb.set_trace()