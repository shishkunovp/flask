from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db: SQLAlchemy = SQLAlchemy(app)

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

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/add_users', methods=['GET', 'POST'])
def add_users():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return f"Пользователь: {username} добавлен"
    return render_template('add_users.html')

if __name__ == '__main__':
    app.run(debug=True)