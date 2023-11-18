from flask import Flask
app=Flask(__name__)

print(__name__)

# flask的路由
@app.route('/')
def index():
    return '<h1>hello world!</h1>'

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return "hello hello"

@app.route('/hi', methods=['get','post'])
def hi():
    return "hi hi"

# 变量规则1
@app.route('/user/<id>')
def index2(id):
    if id=='1':
        return 'python'
    elif id==str(2):
        return 'java'
    elif int(id)==3:
        return 'goLang'
    else:
        return 'hello world'
    
# 变量规则2
@app.route('/dog/<int:id>')
def index3(id):
    if id==1:
        return 'dog A'
    elif id==2:
        return 'dog B'
    elif id==3:
        return 'dog C'
    else:
        return 'Tiger'

if __name__=="__main__":
    app.run()