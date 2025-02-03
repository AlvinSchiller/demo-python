import os
import sys
sys.path.append('.')

from server.webapp import flaskapp, database, cursor, TEMPLATES
from server.models import *
from server.routes import *

default_books = [
    ("The Hobbit", "JRR Tolkien", True, "yes"),
    ("The Fellowship of the Ring", "JRR Tolkien", True, "yes"),
    ("The Eye of the World", "Robert Jordan", False, "yes"),
    ("A Game of Thrones", "George R. R. Martin", True, "yes"),
    ("The Way of Kings", "Brandon Sanderson", False, "yes")
]

env_token = "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"


if __name__ == "__main__":
    cursor.execute(
        '''CREATE TABLE books (name text, author text, read text, test)'''
    )

    for bookname, bookauthor, hasread, booktest in default_books:
        try:
            cursor.execute(
                'INSERT INTO books values (?, ?, ?, ?)',
                (bookname, bookauthor, 'true' if hasread else 'false', booktest)
            )

        except Exception as err:
            print(f'[!] Error Occurred: {err}')

    flaskapp.run('0.0.0.0', debug=bool(os.environ.get('DEBUG', False)))
    
    cursor.close()
    database.close()
