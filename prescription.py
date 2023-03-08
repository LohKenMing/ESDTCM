from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/prescription'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

# there is a self-discovery method but its not covered in this module. FIND IT, else will have to input manually
class Book(db.Model):
    __tablename__ = 'prescriptions'


    date = db.Column(db.String(), primary_key=True)
    orderID = db.Column(db.Integer)
    price = db.Column(db.Float(precision=2))
    status = db.Column(db.String())

    def __init__(self, date, orderID, price, status):
        self.date = date
        self.orderID = orderID
        self.price = price
        self.status = status

    def json(self):
        return {"date": self.date, "orderID": self.orderID, "price": self.price, "status": self.status}


@app.route("/")
def get_all():
    booklist = Book.query.all() # equivalent to SELECT * FROM book
    if len(booklist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "books": [book.json() for book in booklist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no books."
        }
    ), 404



# # <string:isbn13> sets a default valule
# @app.route("/book/<string:isbn13>")
# def find_by_isbn13(isbn13):
#     book = Book.query.filter_by(isbn13=isbn13).first() # SELECT * FROM book WHERE isbn13 = <isbn13> LIMIT 1
#     if book:
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": book.json()
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "message": "Book not found."
#         }
#     ), 404


# @app.route("/book/<string:isbn13>", methods=["POST"])
# def create_book(isbn13):
#     if (Book.query.filter_by(isbn13=isbn13).first()):
#         return jsonify(
#             {
#                 "code": 400,
#                 "data": {
#                     "isbn13": isbn13
#                 },
#                 "message": "Book already exists."
#             }
#         ), 400

#     data = request.get_json()
#     book = Book(isbn13, **data) # **data refers to the Book constructor to set title, availability, etc

#     try:
#         db.session.add(book) # equivalent to INSERT INTO book (isbn13, ...) VALUES (<isbn13>, ...)
#         db.session.commit()
#     except:
#         return jsonify(
#             {
#                 "code": 500,
#                 "data": {
#                     "isbn13": isbn13
#                 },
#                 "message": "An error occurred creating the book."
#             }
#         ), 500

#     return jsonify(
#         {
#             "code": 201,
#             "data": book.json()
#         }
#     ), 201


if __name__ == "__main__":
    app.run(port=5000, debug=True)