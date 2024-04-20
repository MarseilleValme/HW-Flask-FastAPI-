# Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль"
# и кнопку "Зарегистрироваться". При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

app.config['SECRET_KEY'] = b'123456'
csrf = CSRFProtect(app)


# @app.route('/')
# def index():
#     return 'Hi!'


@app.cli.command('init-db')
def init_db():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(firstname=firstname, lastname=lastname, email=email).first()
        if user:
            return 'Такой пользователь уже есть!'
        else:
            new_user = User(firstname=firstname, lastname=lastname, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return 'Пользователь успешно зарегистрирован'
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)