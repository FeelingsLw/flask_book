from book_sys.models import *
from . import db


# -----------------用户操作--------------------
# def do_login(uname, password):
#     user = get_user(uname, password)
#     if user:
#         pass

#
# def get_user(uname, password):
#     user = User.query.filter_by(uname=uname, passwd=password).first()
#     return user




def get_admin(uname, password):
    user = Admin.query.filter_by(name=uname, passwd=password).first()
    return user


def get_student(uname, passwrod):
    stu = Student.query.filter_by(student_name=uname, password=passwrod).first()
    return stu


# -----------------图书操作--------------------
def add_book(book):
    bo = Book.query.filter_by(name=book.name, writer=book.writer, pub_company=book.pub_company).first()
    if bo:
        return 0
    else:
        db.session.add(book)
        db.session.commit()
        return 1


def get_book(id):
    book = Book.query.filter_by(id=id).first()
    return book


def get_books(book_id=None, book_name=None, writer=None, pub_company=None):
    bq = Book.query
    if book_id:
        bq = bq.filter_by(id=book_id)
    if book_name:
        bq = bq.filter_by(name=book_name)
    if writer:
        bq = bq.filter_by(writer=writer)
    if pub_company:
        bq = bq.filter_by(pub_company=pub_company)
    return bq.all()


def remove_book(id):
    result = Book.query.filter_by(id=id).delete()
    db.session.commit()
    return result


def update_book(id, book):
    result = Book.query.filter_by(id=id).update(book)
    db.session.commit()
    return result


def get_sort():
    return Sort.query.all()


# -----------------学生管理--------------------------
def get_stu(name,passwd):
    stu = Student.query.filter_by(name=name,passwd=passwd).first()
    return stu
def get_student(id):
    stu = Student.query.filter_by(id=id).first()
    return stu


def get_students(stu=None):
    if stu:
        pass
    else:
        return Student.query.all()


def remove_student(id, stu):
    result = Student.query.filter_by(id=id).update(stu)
    Book_Student.query.filter_by(student_id=id).delete()
    db.session.commit()
    return result


def loss_student(id, stu):
    result = Student.query.filter_by(id=id).update(stu)
    db.session.commit()
    return result


def update_student(id, stu):
    result = Student.query.filter_by(id=id).update(stu)
    db.session.commit()
    return result


def add_student(student):
    stu = Student.query.filter_by(name=student.name, telephone=student.telephone).first()
    if stu:
        return 0
    else:
        db.session.add(student)
        db.session.commit()
        return 1


def get_college(id=None):
    if id:
        return College.query.filter_by(college_id=id).first()
    else:
        return College.query.all()


def get_class(id=None):
    if id:
        return Class_.query.filter_by(class_id=id).first()
    else:
        return Class_.query.all()


# --------------------------借书查看-------------------------------
def add_book_student(bs):
    book = get_book(bs.book_id)
    if book.current_num > 0:
        book.current_num -= 1
        Book.query.filter_by(id=book.id).update({Book.current_num: book.current_num})
        db.session.add(bs)
        db.session.commit()
        return True
    else:
        return False


def get_book_students(book_id=None, student_id=None):
    bs = Book_Student.query
    if book_id:
        bs = bs.filter_by(book_id=book_id)
    if student_id:
        bs = bs.filter_by(student_id=student_id)
    return bs.all()


def get_book_student(id):
    return Book_Student.query.filter_by(id=id).first()


def do_return_book(id, args):
    book_id = args['book_id']
    args.pop('book_id')
    result = Book_Student.query.filter_by(id=id).update(args)
    book = Book.query.filter_by(id=book_id).first()
    Book.query.filter_by(id=book.id).update({'current_num': book.current_num + 1})
    db.session.commit()
    return result
