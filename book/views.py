from flask import Flask, render_template,request,redirect,url_for
from book import app

@app.route('/')
def main():
    return render_template('common/index.html')
@app.route('/login',methods=['GET','POST'])
def login():

    if request.method=='POST':
        uname = request.form['uname']
        pwd = request.form['passwd']
        print(uname+'---'+pwd)
        return redirect(url_for('main'))
    else:
        return render_template('login.html')

@app.route('/user')
def user():
    return render_template('user.html')



@app.errorhandler(404)
def page_not_found(text):
    return render_template('common/404.html'),404

def create_app():
    app = Flask(__name__)


