from flask import Flask
from flask_restful import Api
from routes import BookList, Book, ReviewsList, Review
<<<<<<< HEAD
from flask_cors import CORS

BASE_URL = '/api/bookreactions'
=======

BASE_URL = '/api/bookreactions'
api = Api(app)
api.add_resource(BookList, f'{BASE_URL}/Books/<book_id>')
api.add_resource(Book, f'{BASE_URL}/Book')
api.add_resource(ReviewsList, f'{BASE_URL}/Reviews/<book_id>')
api.add_resource(Review, f'{BASE_URL}/Review')
>>>>>>> c6adb7f07b848bae3ea85557f90dc4252fba99b4
app = Flask(__name__)
CORS(app)

<<<<<<< HEAD
api = Api(app)
api.add_resource(BookList, f'{BASE_URL}/Books/')
api.add_resource(Book, f'{BASE_URL}/Book/<book_id>')
api.add_resource(ReviewsList, f'{BASE_URL}/Reviews/<book_id>')
api.add_resource(Review, f'{BASE_URL}/Reviews/')
=======
@app.route('/')
def hello_world():
    return 'Hello, flask debugging world'
>>>>>>> c6adb7f07b848bae3ea85557f90dc4252fba99b4

if __name__ == '__main__':
    app.run(debug=True)
