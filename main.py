import random
import string
from datetime import datetime

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'

db = SQLAlchemy(app)


class URLmodel(db.Model):
    __tablename__ = 'ur_lmodel'
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), unique=True)
    short = db.Column(db.String(6), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    visits = db.Column(db.Integer, default=0)


class URLForm(FlaskForm):
    original_url = StringField(
        'Вставьте ссылку',
        validators=[DataRequired(message="Ссылка не может быть пустой"),
                    URL(message='Неверная ссылка')]
    )
    submit = SubmitField('Получить короткую ссылку')


# Создание базы данных (выполняйте только один раз)
with app.app_context():
    db.create_all()


def get_short():
    while True:
        short = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        if URLmodel.query.filter(URLmodel.short == short).first():
            continue
        return short


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        url = URLmodel()
        url.original_url = form.original_url.data
        url.short = get_short()
        db.session.add(url)
        db.session.commit()
        return redirect(url_for('urls'))
    return render_template('index.html', form=form)


@app.route('/urls', methods=['GET'])
def urls():
    urls = URLmodel.query.all()
    return render_template('urls.html', urls=urls[::-1])


@app.route('/<string:short>', methods=['GET'])
def url_redirect(short):
    url = URLmodel.query.filter(URLmodel.short == short).first()
    if url:
        url.visits += 1  # Исправлено с url.visit на url.visits
        db.session.add(url)
        db.session.commit()
        return redirect(url.original_url)
    return "URL not found", 404  # Добавлена обработка случая, когда URL не найден


if __name__ == '__main__':
    app.run(debug=True, port=5004)