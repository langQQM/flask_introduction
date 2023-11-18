# 重定向 302
# 两种方式：redirect, url_for

from flask import Flask, redirect,url_for

app=Flask(__name__)

@app.route('/index')
def index():
    # return redirect('https://www.baidu.com')
    return redirect(url_for('hello'))

@app.route('/abc')
def hello():
    return 'this is hello fun'

if __name__ == '__main__':
    app.run()