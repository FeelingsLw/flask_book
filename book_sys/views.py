from flask import Flask, render_template, request, redirect, url_for
from book_sys import app
from .models import *
from .servies import *


@app.route('/')
def main():
    return render_template('common/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['passwd']
        print(uname + '---' + pwd)
        return redirect(url_for('main'))
    else:
        return render_template('login.html')


@app.route('/user')
def user():
    return render_template('user.html')


@app.errorhandler(404)
def page_not_found(text):
    return render_template('common/404.html'), 404


@app.route('/book/add/')
def book_add(book):

    sorts = get_sort()
    #print(sorts)
    return render_template('book/add.html',sorts=sorts)

@app.route('/book/do_add/')
def book_do_add():
    return "SUCCESS"
    # book = Book()
    # book.book_name='Python'
    # book.writer = 'zs'
    # book.sort_id =1
    # book.price = 1
    # book.pub_company = '图灵'
    # book.pub_date = '2018-01-01'
    # book.total_num = 2
    # book.current_num = 2
    # book.buy_date = '2018-01-01'
    # book.brief = '100'
    #
    # add_book(book)
