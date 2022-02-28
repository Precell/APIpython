from models import BookModel, ReviewModel
from flask import Flask
import psycopg2
from psycopg2 import pool
from repository import Repository
from unittest import MagicMock

book1 = BookModel("The Hobbit", "J R R Tolkien", 1)
book2 = BookModel("The Lord Of The Rings", "J R R Tolkien", 2)
review1 = ReviewModel("a timeless classic", 1)
review2 = ReviewModel("I hated it", 2)
review3 = ReviewModel("an even more timeless classic", 3)
review4 = ReviewModel("I hated it even more", 4)

book_row = [
    (book1.title, book1.author, book1.bookId, book1.cover),
    (book1.title, book1.author, book1.bookId, book1.cover)
]