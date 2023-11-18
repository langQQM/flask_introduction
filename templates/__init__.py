from flask import Flask, make_response, json, jsonify

app=Flask(__name__)
# app.config['JSON_AS_ASCII'] = False
# 古い書き方で、かきのように書きます。
app.json.ensure_ascii=False

@app.route('/index')
def index():
    data={
        'name':'张三'
    }
    # response=make_response(json.dumps(data, ensure_ascii=False))
    # response.mimetype='application/json'
    # return response
    return jsonify(data)

if __name__ == '__main__':
    app.run()