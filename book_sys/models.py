from book_sys import db


class Book(db.Model):
    __tablename__='t_book'
    book_num = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(20))
    writer = db.Column(db.String(10))
    sort_id = db.Column(db.String(5))
    price = db.Column(db.Integer)
    pub_company = db.Column(db.String(20))
    pub_date = db.Column(db.DATE)
    total_num = db.Column(db.INT)
    current_num = db.Column(db.Integer)
    buy_date = db.Column(db.DATE)
    brief = db.Column(db.String(100))


class Student(db.Model):
    __tablename__ = 't_student'
    student_num = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(10))
    password = db.Column(db.String(20))
    academy_id = db.Column(db.Integer,db.ForeignKey('college.id'))
    class_id = db.Column(db.Integer,db.ForeignKey('class_.id'))
    sex = db.Column(db.String(2))
    telephone = db.Column(db.String(15))
    email = db.Column(db.String(20))
    lended_num = db.Column(db.Integer)
    create_date = db.Column(db.DATE)


class Admin(db.Model):
    __tablename__ = 't_admin'
    admin_id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String(10))
    admin_password = db.Column(db.String(20))


class College(db.Model):
    __tablename__ = 't_college'
    college_id = db.Column(db.Integer, primary_key=True)
    college_name = db.Column(db.String(30))


class Class_(db.Model):
    __tablename__ = 't_class'
    class_id = db.Column(db.INT, primary_key=True)
    class_name = db.Column(db.String(30))
    college_id = db.Column(db.Integer,db.ForeignKey('college.id'))


class Sort(db.Model):
    __tablename__ = 't_sort'
    sort_id = db.Column(db.Integer, primary_key=True)
    sort_name = db.Column(db.String(20))
