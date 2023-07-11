import json
from flask import Flask, request, jsonify
import sqlite3
import os

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to mi API conected to my books database"

# 0.Ruta para obtener todos los libros


@app.route('/api/v1/resources/books/all', methods=['GET'])
def get_all():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    query = "SELECT * from books"
    result = cursor.execute(query).fetchall()
    connection.close()
    return jsonify(result)

# 1. Route to get the count of books by author ordered in descending order


@app.route('/api/v1/resources/booksbyauthor/', methods=['GET'])
def books_by_author():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    query = "SELECT author, COUNT(*) as count FROM books GROUP BY author ORDER BY count DESC"
    result = cursor.execute(query).fetchall()
    connection.close()
    return jsonify(result)


# 2. Route to get the books of an author as an argument in the call
@app.route('/api/v1/resources/books/author', methods=['GET'])
def books_by_author_arg():
    author = request.args.get('author')
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    query = "SELECT * FROM books WHERE author=?"
    result = cursor.execute(query, (author,)).fetchall()
    connection.close()
    return jsonify(result)

# 3. Route to get the books filtered by title, publication and author


@app.route('/api/v1/resources/books/filters', methods=['GET'])
def books_by_filters():
    title = request.args.get('title')
    published = request.args.get('published')
    author = request.args.get('author')
    query = "SELECT * FROM books WHERE title=? AND published=? AND author=?"
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    result = cursor.execute(query, (title, published, author)).fetchall()
    connection.close()
    return jsonify(result)


# Este puerto si funciona
app.run(port=8000)
