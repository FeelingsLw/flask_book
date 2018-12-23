from book_sys import db
from sqlalchemy.ext.declarative import declarative_base  # 用于创建基础类

Base = declarative_base()


class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30))
    passwd = db.Column(db.String(255))


class Role(db.Model):
    __tablename__ = 't_role'
    id = db.Column(db.Integer, primary_key=True)


class Book(db.Model):
    __tablename__ = 't_book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    writer = db.Column(db.String(10))
    sort_id = db.Column(db.String(5), db.ForeignKey('t_sort.id'))
    price = db.Column(db.Integer)
    pub_company = db.Column(db.String(20))
    pub_date = db.Column(db.DATE)
    total_num = db.Column(db.INT)
    current_num = db.Column(db.Integer)
    buy_date = db.Column(db.DATE)
    brief = db.Column(db.String(100))

    sort = db.relationship('Sort', backref=db.backref('books', lazy=True))
    book_student = db.relationship('Book_Student', back_populates='book')


class Student(db.Model):
    __tablename__ = 't_student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    college_id = db.Column(db.Integer, db.ForeignKey('t_college.id'))
    class_id = db.Column(db.Integer, db.ForeignKey('t_class.id'))
    sex = db.Column(db.String(2))
    telephone = db.Column(db.String(15))
    email = db.Column(db.String(20))
    lended_num = db.Column(db.Integer)
    create_date = db.Column(db.DATE)

    college = db.relationship("College", backref=db.backref('students', lazy=True))
    class_ = db.relationship("Class_", backref=db.backref('students', lazy=True))

    book_student = db.relationship('Book_Student', back_populates='student')


class Admin(db.Model):
    __tablename__ = 't_admin'
    admin_id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String(10))
    admin_password = db.Column(db.String(20))


class College(db.Model):
    __tablename__ = 't_college'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    student = db.relationship("Student", back_populates='college')


class Class_(db.Model):
    __tablename__ = 't_class'
    id = db.Column(db.INT, primary_key=True)
    name = db.Column(db.String(30))
    student = db.relationship("Student", back_populates='class_')


class Sort(db.Model):
    __tablename__ = 't_sort'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    book = db.relationship('Book', back_populates='sort')


class Book_Student(db.Model):
    __tablename__ = 't_book_student'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('t_book.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('t_student.id'))
    borrow_date = db.Column(db.DATE)
    return_date = db.Column(db.DATE)
    money = db.Column(db.Integer)

    book = db.relationship('Book', back_populates='book_student', uselist=False)
    student = db.relationship('Student', back_populates='book_student', uselist=False)
