from flask import request
from app import app
from unittest.mock import MagicMock
from repository import Repository
from routes import BookList, Book, ReviewsList, Review
from models import BookModel, ReviewModel

book1 = BookModel("Test The Hobbit", "J R R Tolkien", 1)
book2 = BookModel("Test The Lord Of The Rings", "J R R Tolkien", 2)
book2 = BookModel("Test Elementary", "Kevin Rattan", )
review1 = ReviewModel("Test a timeless classic", 1)
review2 = ReviewModel("Test I hated it", 2)
review3 = ReviewModel("Test an even more timeless classic", 3)
review4 = ReviewModel("Test I hated it even more", 4)

def test_booklist_get():
    repo = MagicMock(spec=Repository)
    repo.books_get_all.return_value = [book1, book2]
    books = BookList(repo).get()
    assert books[0]['bookId'] == 1
    assert books[1]['title'] == 'test The Lord Of The'
    
# def test_booklist_post():
#     with app.test_request_context():
#         repo =MagicMock(spec=Repository)
#         req = MagicMock(spec=request)
#         data = BookModel('Elementary', 'Kevin Rattan', 100)
#         req.json.return_value = data.__dict__
#         book = BookList(repo).post(req)
#         assert int(book['bookId']) == 100
#         assert book['title'] == 'Elementary'
        