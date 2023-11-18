# raise 主动抛出异常
# abort 在网页当中抛出异常

from flask import Flask,abort,request,make_response,render_template

app=Flask(__name__)

@app.route('/index', methods=['GET','POST'])
def index():
    if request.method=='GET':
        print('get')
        # return make_response('index.html')
        return render_template('index.html')
    if request.method=='POST':
        print('post')
        name=request.form.get('name')
        password=request.form.get('password')
        if name=='zhangsan' and password == '123':
            return 'login success'
        else:
            # abort(404)
            # return None
            return render_template('404.html')
    # abort(404)
    # return '123'

# 自定义错误处理方法
@app.errorhandler(404)
def handle_404_error(err):
    return '出现了404错误 错误信息是%s'%err
if __name__ == '__main__':
    app.run()