from distutils.log import error
from select import select
from turtle import title
import psycopg2
from models import BookModel, ReviewModel
import os

book1 = BookModel("The Hobbit", "J R R Tolkien", 1)
book2 = BookModel("The Lord Of The Rings", "J R R Tolkien", 2)
review1 = ReviewModel("a timeless classic", 1)
review2 = ReviewModel("I hated it", 2)
review3 = ReviewModel("an even more timeless classic", 3)
review4 = ReviewModel("I hated it even more", 4)

HOST = os.environ.get("HOST")
DATABASE = os.environ.get("DATABASE")
DB_PORT = os.environ.get("DB_PORT")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")

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
              book_list = []
              for row in book_records:
                  book_list.append(BookModel(row[0],row[1],row[2]))
                  
              ps_cursor.close()
            return book1          
        except Exception as error:
            print(error)  
        finally:
            if conn is not None:
                conn.close()
                
    def book_add(self, data):
            
        conn = None
        try:
            conn = self.get_db()
            if (conn):
              ps_cursor = conn.cursor()
              ps_cursor.execute(
                  "INSERT INTO book(title, cover, author) VALUES(%s, %s, %s) RETURNING bookId",
                  (data['title'], data['cover'], data['author'])
              )
              conn.commit()
              id = ps_cursor.fetchone()[0]
              ps_cursor.close()          
              book = BookModel(data['title'], id, data['author'], data['cover'])
        except Exception as error:
            print(error)  
        finally:
            if conn is not None:
                conn.close()
    
    def book_get_by_id(self, book_id):
        books = [book1, book2]
        return next((x for x in books if x.bookId == book_id), None)
    
    def reviews_get_all(self):
        conn = None
        try:
            conn = self.get_db
            if(conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute(
                    ""
                )  
    def reviews_get_by_book_id(self, book_id):
        reviews = [review1, review2, review3, review4]
        return [x for x in reviews if x.book_id == book_id ]

    def review_add(self,data):
        return ReviewModel(data['content'], data['bookId'], 1)
    
  