from flask import Flask, request, render_template


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

@app.route('/page')
def page():
    return render_template('index.html', name='Flask')

if __name__ == '__main__':
    app.run(debug=True)