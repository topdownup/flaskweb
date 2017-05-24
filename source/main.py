#coding=utf-8
from flask import Flask, request,template_rendered


app = Flask(__name__)


@app.route('/hello')
def say_hello():
    return "hello world"


@app.route('/')
@app.route('/index')
def index():
    user = {"name":"wowo","age":11}
    return template_rendered('index.html',title='title name',user=user)


@app.route('/show_user/<username>')
def show_user(username):
    return "User is %s" % username


@app.route('/show_id/<int:id>')
def show_id(id):
    return "ID is %d" % id


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "post"
    else:
        return "get"


if __name__ == "__main__":
    app.run(host='192.168.50.237')
