from flask import Flask
from flask_restful import Api
from routes import BookList, Book, ReviewsList, Review
from flask_cors import CORS
import os

BASE_URL = os.environ.get("BASE_URL")
app = Flask(__name__)
CORS(app)

api = Api(app)
api.add_resource(BookList, f'{BASE_URL}/Books/')
api.add_resource(Book, f'{BASE_URL}/Book/<book_id>')
api.add_resource(ReviewsList, f'{BASE_URL}/Reviews/<book_id>')
api.add_resource(Review, f'{BASE_URL}/Reviews/')

if __name__ == '__main__':
    app.run(debug=True)
