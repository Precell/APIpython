from flask import Flask
from flask_restful import Api
from routes import BookList, Book, ReviewsList, Review

BASE_URL = '/api/bookreactions'
api = Api(app)
api.add_resource(BookList, f'{BASE_URL}/Books/<book_id>')
api.add_resource(Book, f'{BASE_URL}/Book')
api.add_resource(ReviewsList, f'{BASE_URL}/Reviews/<book_id>')
api.add_resource(Review, f'{BASE_URL}/Review')
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, flask debugging world'

if __name__ == '__main__':
    app.run(debug=True)
