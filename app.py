from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    return "Привет, Flask!"

@app.route('/hello/<name>')
def say_hello(name):
    return f"Hello, {name}!"


@app.route('/calc', methods=['POST'])
def calc_sum():
    data = request.get_json()
    a = data['a']
    b = data['b']
    return {'result': a + b}

if __name__ == '__main__':
    app.run(debug=True)