from distutils.log import error
from select import select
from turtle import title
import psycopg2
from models import BookModel, ReviewModel
from flask import current_app, g

book1 = BookModel("The Hobbit", "J R R Tolkien", 1)
book2 = BookModel("The Lord Of The Rings", "J R R Tolkien", 2)
review1 = ReviewModel("a timeless classic", 1)
review2 = ReviewModel("I hated it", 2)
review3 = ReviewModel("an even more timeless classic", 3)
review4 = ReviewModel("I hated it even more", 4)


class Repository():
    def get_db(self):
       if 'db' not in g:
           g.db = current_app.config['pSQL_pool'].getconn()
           return g.db
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
            return book_list          
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
                    "select content, bookId,"
                ) 
                review_records = ps_cursor.fetchall()
                book_review = []
                for row in review_records:
                    book_review.append(ReviewModel(row[0], row[1]))
            return book_review
        except Exception as error:
            print(error)     
        finally:
            if conn is None:
                conn.close()
                              
    def reviews_get_by_book_id(self, book_id):
        reviews = [review1, review2, review3, review4]
        return [x for x in reviews if x.book_id == book_id ]

    def review_add(self,data):
        conn = None
        try:
            conn = self.get_db()
            if (conn):
              ps_cursor = conn.cursor()
              ps_cursor.execute(
                  "INSERT INTO review(content) VALUES(%s) RETURNING bookId",
                  (data['content'])
              )
              conn.commit()
              id = ps_cursor.fetchone()[0]
              ps_cursor.close()          
              review = (data['content'])
        except Exception as error:
            print(error)  
        finally:
            if conn is not None:
                conn.close()
  