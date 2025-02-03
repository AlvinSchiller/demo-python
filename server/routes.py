
from flask import request, render_template, make_response

from server.webapp import flaskapp, cursor
from server.models import Book


@flaskapp.route('/')
def index():
    name = request.args.get('name')
    author = request.args.get('author')
    read = bool(request.args.get('read'))
    test = bool(request.args.get('test'))
    test2 = bool(request.args.get('test2'))

    if name:
        cursor.execute(
            "SELECT * FROM books WHERE name LIKE '%" + name + "%'"
        )
        books = [Book(*row) for row in cursor]

    elif author:
        cursor.execute(
            "SELECT * FROM books WHERE author LIKE '%" + author + "%'"
        )
        books = [Book(*row) for row in cursor]

    elif test:
        cursor.execute(
            "SELECT * FROM books WHERE test LIKE '%" + test + "%'"
        )
        books = [Book(*row) for row in cursor]

    elif test2:
        cursor.execute(
            "SELECT * FROM books WHERE test2 LIKE '%" + test2 + "%'"
        )
        books = [Book(*row) for row in cursor]
    else:
        cursor.execute("SELECT name, author, read, test, test2 FROM books")
        books = [Book(*row) for row in cursor]

    return render_template('books.html', books=books)
