from select import select
from turtle import title
from psycopg2 import  psycopg2
from models import BookModel, ReviewModel

book1 = BookModel("The Hobbit", "J R R Tolkien", 1)
book2 = BookModel("The Lord Of The Rings", "J R R Tolkien", 2)
review1 = ReviewModel("a timeless classic", 1)
review2 = ReviewModel("I hated it", 2)
review3 = ReviewModel("an even more timeless classic", 3)
review4 = ReviewModel("I hated it even more", 4)

HOST = '12.0.0.1'
DATABASE = 'bookreactions'
DB_PORT = 5432
USER = 'postgres'
PASSWORD = 'precell'

class Repository():
    def get_db(self):
        return psycopg2.Connect(
            host = HOST,
            database = DATABASE,
            port = DB_PORT,
            user = USER,
            password = PASSWORD
        )
    def books_get_all(self):
        conn = None
        try:
            conn = self.get_db()
            if (conn):
              ps_cursor = conn.cursor()
              ps_cursor.execute("select title, author, bookId, cover")
              book_records = ps_cursor.fetchall()  
        except Exception as error:
            
        finally:        
    
    def book_get_by_id(self, book_id):
        books = [book1, book2]
        return next((x for x in books if x.bookId == book_id), None)
    
    def reviews_get_all(self):
        return [review1, review2, review3, review4]
    
    def reviews_get_by_book_id(self, book_id):
        reviews = [review1, review2, review3, review4]
        return [x for x in reviews if x.book_id == book_id ]

    def review_add(self,data):
        return ReviewModel(data['content'], data['bookId'], 1)
    
    def book_add(self, data):
        return BookModel(data['title'], data['cover'], 3, data['author'])
