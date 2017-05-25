# coding=utf-8
from flask import request, render_template, flash, redirect
from source import app
from .forms import LoginForm

@app.route('/hello')
def say_hello():
    return "hello world"


@app.route('/')
@app.route('/index')
def index():
    user = {"name": "wowo", "age": 11}
    posts = [{"author": {"nickname": "张三"},
              "say": "你好"},
             {"author": {"nickname": "李四"},
              "say": "好天气"}]
    return render_template("index.html", title='title name', user=user, posts=posts)


@app.route('/show_user/<username>')
def show_user(username):
    return "User is %s" % username


@app.route('/show_id/<int:id>')
def show_id(id):
    return "ID is %d" % id


@app.route('/login', methods=['GET', 'POST'])
def login():
    # form = LoginForm()
    form = LoginForm(request.form)
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect("/index")
    # else:
    #     return redirect("/error")
    if request.method == 'POST':
        return "post"
    else:
        return render_template("login.html",title="login title",form = form,providers = app.config['OPENID_PROVIDERS'])


# if __name__ == "__main__":
#     app.run(host='192.168.50.237')
