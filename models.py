class BookModel:
<<<<<<< HEAD
    def __init__(self, title, author, bookId = -1, cover=''):
        self.title = title
        self.author = author
        self.bookId = bookId
=======
    def __init__(self, title, author, id = -1, cover=''):
        self.title = title
        self.author = author
        self.id = id
>>>>>>> c6adb7f07b848bae3ea85557f90dc4252fba99b4
        self.cover = cover
       
class ReviewModel:
    def __init__(self, content, bookId, id=-1):
        self.content = content
        self.bookId = bookId
        self.id = id        