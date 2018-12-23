from flask import Flask, render_template, request, redirect, url_for
from book_sys import app
from .models import *
from .servies import *
import datetime


@app.route('/')
def main():
    return render_template('common/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['passwd']
        print(uname + '---' + pwd)
        user = get_user(uname, pwd)
        return redirect(url_for('main'))
    else:
        return render_template('login.html')


@app.route('/user')
def user():
    return render_template('user.html')


@app.errorhandler(404)
def page_not_found(text):
    return render_template('common/404.html'), 404


# -----------------图书操作--------------------

@app.route('/book/list/', methods=['GET', 'POST'])
def book_list():
    if request.method == 'GET':
        books = get_books()
        return render_template('book/list.html', books=books)
    else:
        book_id = None
        book_name = None
        if request.form:
            for key in dict(request.form).keys():
                if "book_id" == key:
                    book_id = request.form[key]
                elif "book_name" == key:
                    book_name = request.form[key]
        books= get_books(book_id,book_name)
        return render_template('book/list.html', books=books)


@app.route('/book/remove/<int:id>/')
def book_remove(id):
    result = remove_book(id)
    if result > 0:
        return render_template('common/massage.html', msg='图书删除成功')

    else:
        return render_template('common/massage.html', msg='图书删除失败')


@app.route('/book/add/')
def book_add():
    sorts = get_sort()
    return render_template('book/add.html', sorts=sorts)


@app.route('/book/do_add/', methods=['POST'])
def book_do_add():
    book = Book()
    book.name = request.form['name']
    book.writer = request.form['writer']
    book.sort_id = request.form['sort_id']
    book.price = request.form['price']
    book.pub_company = request.form['pub_company']
    book.pub_date = request.form['pub_date']
    book.brief = request.form['brief']
    book.total_num = request.form['total_num']
    book.current_num = request.form['total_num']
    book.buy_date = datetime.datetime.now().strftime('%Y-%m-%d')
    result = add_book(book)
    if result > 0:
        return render_template('common/massage.html', msg='图书增加成功')

    else:
        return render_template('common/massage.html', msg='图书增加失败')


@app.route('/book/update/<int:id>/')
def book_update(id):
    book = get_book(id)
    sorts = get_sort()
    return render_template('book/update.html', book=book, sorts=sorts)


@app.route('/book/do_update/<int:id>/')
def book_do_update(id):
    args = {}
    for key in dict(request.form).keys():
        args[key] = request.form[key]
    result = update_book(id, args)
    if result > 0:
        return render_template('common/massage.html', msg='图书修改成功')

    else:
        return render_template('common/massage.html', msg='图书修改失败')


# --------------------借书证--------------------------

@app.route('/student/list/')
def student_list():
    students = get_students()
    return render_template('student/list.html', students=students)


@app.route('/student/remove/<int:id>/')
def student_remove(id):
    result = remove_student(id)
    if result > 0:
        return render_template('common/massage.html', msg='图书删除成功')

    else:
        return render_template('common/massage.html', msg='图书删除失败')


@app.route('/student/add/')
def student_add():
    colleges = get_college()
    clases = get_class()
    return render_template('student/add.html', colleges=colleges, clases=clases)


@app.route('/student/do_add/', methods=['POST'])
def student_do_add():
    args = {}
    stu = Student()
    stu.name = request.form['name']
    stu.college_id = request.form['college_id']
    stu.class_id = request.form['class_id']
    stu.sex = request.form['sex']
    stu.telephone = request.form['telephone']
    stu.email = request.form['email']
    stu.lended_num = request.form['lended_num']
    stu.create_date = request.form['create_date']
    result = add_student(stu)
    if result > 0:
        return render_template('common/massage.html', msg='借书证增加成功')

    else:
        return render_template('common/massage.html', msg='借证书增加失败')


@app.route('/student/update/<int:id>/')
def student_update(id):
    student = get_student(id)
    colleges = get_college()
    clases = get_class()
    return render_template('student/update.html', student=student, colleges=colleges, clases=clases)


@app.route('/student/do_update/<int:id>/', methods=['POST'])
def student_do_update(id):
    args = {}
    for key in dict(request.form).keys():
        args[key] = request.form[key]
    result = update_student(id, args)
    if result > 0:
        return render_template('common/massage.html', msg='借证书修改成功')

    else:
        return render_template('common/massage.html', msg='借证书修改失败')


# -----------------借书模块----------------------
@app.route('/book_student/book_list/',methods=['GET','POST'])
def get_book_student_book_list():
    books=[]
    if request.method == 'GET':
        books = get_books()
    else:
        book_id = None
        book_name = None
        if request.form:
            for key in dict(request.form).keys():
                if "id" == key:
                    book_id = request.form[key]
                elif "name" == key:
                    book_name = request.form[key]
        books= get_books(book_id,book_name)
    return render_template('book_student/book_list.html', books=books)


@app.route('/book_student/add/<int:id>/')
def book_student_add(id):
    book = get_book(id)
    return render_template('book_student/add.html', book=book)


@app.route('/book_student/do_add/', methods=['POST'])
def book_student_do_add():
    bs = Book_Student()
    bs.book_id = request.form['book_id']
    bs.student_id = request.form['student_id']
    bs.borrow_date = request.form['borrow_date']
    reuslt = add_book_student(bs)
    if reuslt:
        return render_template('common/massage.html', msg='借书成功')
    else:
        return render_template('common/massage.html', msg='借书失败')


@app.route('/book_student/return_list/', methods=['POST', 'GET'])
def get_book_student_return_list():
    book_id = None
    student_id = None
    if request.form:
        for key in dict(request.form).keys():
            if "book_id" == key:
                book_id = request.form[key]
            elif "student_id" == key:
                student_id = request.form[key]

    book_student_list = get_book_students(book_id, student_id)
    return render_template('book_student/return_list.html', book_student_list=book_student_list)


@app.route('/book_student/return/<int:id>/')
def book_student_return(id):
    book_student = get_book_student(id)
    return render_template('book_student/return.html', bs=book_student)


@app.route('/book_student/do_return/<int:id>/', methods=['POST'])
def book_student_do_return(id):
    args = {}
    for key in dict(request.form).keys():
        args[key] = request.form[key]
    result = do_return_book(id, args)
    if result > 0:
        return render_template('common/massage.html', msg='还书成功')

    else:
        return render_template('common/massage.html', msg='还书失败')
