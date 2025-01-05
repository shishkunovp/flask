from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Flask')

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
    return render_template('page.html', name='Страница 1')

@app.route('/about')
def about():
    return render_template('about.html', name='О нас')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Здесь можно добавить логику проверки/сохранения
        return f"Регистрация успешна. Пользователь: {username}"
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)