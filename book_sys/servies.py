from book_sys.models import *
from . import db


def add_book(book):
    db.session.add(book)
    db.session.commit()


def get_sort():
    return Sort.query.all()