from book_sys.models import *
from . import db


# -----------------用户操作--------------------
def do_login(uname, password):
    user = get_user(uname, password)
    if user:
        pass


def get_user(uname, password):
    user = User.query.filter_by(uname=uname, passwd=password).first()
    return user


def get_role_by_user(user):
    pass


def get_admin(uname, password):
    user = Admin.query.filter_by(admin_name=uname, admin_password=password).first()
    return user


def get_student(uname, passwrod):
    stu = Student.query.filter_by(student_name=uname, password=passwrod).first()
    return stu


# -----------------图书操作--------------------
def add_book(book):
    bo = Book.query.filter_by(book_name=book.book_name, writer=book.writer, pub_company=book.pub_company).first()
    if bo:
        return 0
    else:
        result = db.session.add(book)
        db.session.commit()
        return 1

def get_book(id):
    book = Book.query.filter_by(book_num=id).first()
    return book

def get_books(book=None):
    if book:
        pass
    else:
        return Book.query.all()

def remove_book(id):
    result = Book.query.filter_by(book_num=id).delete()
    db.session.commit()
    return result


def update_book(id,book):
    result = Book.query.filter_by(book_num=id).update(book)
    #db.session.commit()
    return result




def get_sort():
    return Sort.query.all()
