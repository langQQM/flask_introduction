# 重定向 302

from flask import Flask, redirect

app=Flask(__name__)

@app.route('/index')
def index():
    return redirect('https://www.baidu.com')


if __name__ == '__main__':
    app.run()