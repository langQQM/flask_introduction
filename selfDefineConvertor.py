import typing as t
from werkzeug.routing import BaseConverter
from flask import Flask
from werkzeug.routing.map import Map

app=Flask(__name__)

class RegexConverter(BaseConverter):
    # 自定义转换器类
    def __init__(self,url_map,regex):
        #调用父类的方法
        # super().__init__(url_map)
        super(RegexConverter,self).__init__(url_map)
        self.regex=regex

    def to_python(self, value: str) -> t.Any:
        # 父类的方法 功能已经实现好了
        print("to_python方法被调用")
        # return super().to_python(value) 
        return value


# 将自定义的转换器类添加到flask应用中
app.url_map.converters['re']=RegexConverter
# {'re':RegexConverter}
@app.route('/index/<re("1\d{3}"):value>')
def index(value):
    print(value)
    return 'hello'

if __name__ == '__main__':
    app.run()