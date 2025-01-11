from typing import List, Any

from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'

db = SQLAlchemy(app)

# Модель User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # храним хеш

# Настраиваем LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # куда переходит, если @login_required

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Роут логина
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect('/profile')
        return "Неверный логин или пароль"
    return render_template('login.html')

# Роут логаута
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "Вы вышли из учётной записи."

# Защищённая страница
@app.route('/profile')
@login_required
def profile():
    return f"Привет, {current_user.username}!"

# Не забудьте про шифрование паролей
from werkzeug.security import generate_password_hash, check_password_hash

# Если нужно зарегистрировать пользователя, можно сделать:
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hash_pwd = generate_password_hash(password)
        new_user = User(username=username, password=hash_pwd)
        db.session.add(new_user)
        db.session.commit()
        return "Регистрация успешна."
    users = User.query.all()
    return render_template('register.html',users=users)

if __name__ == '__main__':
    app.run(debug=True)