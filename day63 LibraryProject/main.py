import sqlite3

from flask import Flask, request,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from sqlalchemy import create_engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 
On Windows type:
python -m pip install -r requirements.txt
On MacOS type:
pip3 install -r requirements.txt
This will install the packages from requirements.txt for this project.
'''

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_name = request.form.get('book_name')
        book_author = request.form.get('book_author')
        rating = request.form.get('rating')
        all_books.append({
            "title": book_name,
            "author": book_author,
            "rating": rating
        })
        print(all_books, "Success!")
        return render_template('index.html', all_books=all_books)
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

