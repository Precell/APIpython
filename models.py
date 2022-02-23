class BookModel:
    def __init__(self, title, author, bookId = -1, cover=''):
        self.title = title
        self.author = author
        self.bookId = bookId
        self.cover = cover
       
class ReviewModel:
    def __init__(self, content, bookId, id=-1):
        self.content = content
        self.bookId = bookId
        self.id = id        