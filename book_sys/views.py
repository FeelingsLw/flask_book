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


@app.route('/book/list/')
def book_list():
    books = get_books()
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
    book.book_name = request.form['name']
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
    args={}
    for key in dict(request.form).keys():
        args[key]=request.form[key]
    result = update_book(id,args)
    if result > 0:
        return render_template('common/massage.html', msg='图书修改成功')

    else:
        return render_template('common/massage.html', msg='图书修改失败')