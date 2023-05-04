from data import db_session
from flask import Flask, request
from data.category_table import Category
from data.prof_in_cat import Proff
from data.pass_table import SingUp
import requests
import json

app = Flask(__name__)


@app.route('/user_data_sing_up', methods=['POST'])
def sing_up_user():
    if request.method == 'POST':
        data = request.json  # ['name', 'email', 'password', 'old']
        db_sess = db_session.create_session()  # подключаемся к бд
        obj = SingUp()
        obj.name = data[0]
        obj.email = data[1]
        obj.password = data[2]
        obj.old = data[3]
        db_sess.add(obj)
        db_sess.commit()


def let_sing_in_up(data):
    user_email, user_passw = data[0], data[1]
    db_sess = db_session.create_session()
    data_from_db = []
    user_sing_up = db_sess.query(SingUp).filter(SingUp.email == user_email, SingUp.password == user_passw).first()
    if user_sing_up is not None:
        user_sing_up = db_sess.query(SingUp).filter(SingUp.email == user_email).first()
        if user_sing_up is not None:
            return 2  # такой почты еще нет - можно зарегистрироваться
        else:
            return 1  # такая почта уже зарегистрирована - надо использовать другую/войти с паролем
    else:
        return 3  # есть такая почта и лоогин - пользователь уже зареган/можно войти


@app.route('/', methods=['POST'])
def first():
    if request.method == 'POST':  # ['email', 'password']
        data = request.json  # ЗДЕСЬ МОЖЕТ БЫТЬ ОШИБКА В ЗАВИСИМОСТИ ОТ ДАННЫХ КОТОРЫЕ СКИНУТ
        return let_sing_in_up(data)  # возвращать надо ответ с паролем - подходит/не подходит


def send_to_srv():
    url = 'http://127.0.0.1:5000/'
    param = {'some': 'data'}
    json_param = json.dumps(param)
    resp = requests.post(url, data=json_param)


def profession_json(id_c):  # упаковка в json всех профессий из каталога
    json_sp = []
    db_sess = db_session.create_session()
    for prof in db_sess.query(Proff).filter(Proff.id_category == int(id_c)):
        sp_prof = str(prof).split('/')
        pr = {
            'name': sp_prof[0],
            'zp': sp_prof[1],
            'discr': sp_prof[2]
        }
        json_sp.append(pr)
    # with open('cats.json', 'w', encoding='utf-8') as file:
    #     json.dump(json_sp, file, ensure_ascii=False, indent=2)
    return str(json_sp)


def profession_id(name_category):
    db_sess = db_session.create_session()
    try:
        el_from_db = db_sess.query(Category).filter(Category.name_c == name_category).first()
        return profession_json(el_from_db.id_c)
    except Exception as e:
        print(e)


@app.route('/ebash/<name_category>')
def ebash(name_category):
    return profession_id(name_category)


def main():
    db_session.global_init("db/main_db.db")
    # let_sing_in_up(['aaa', 'bjb'])
    # selenium_find_category()  # чтобы загрузить категории профессий в бд
    app.run()
    send_to_srv()


if __name__ == '__main__':
    main()
    app.run(port=5000, host='0.0.0.0')
