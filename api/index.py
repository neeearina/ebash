from data import db_session
from flask import Flask
from data.category_table import Category
from data.prof_in_cat import Proff
import requests
import json

app = Flask(__name__)


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
    # selenium_find_category()  # чтобы загрузить категории профессий в бд
    app.run()
    send_to_srv()


if __name__ == '__main__':
    main()
    app.run(port=5000, host='0.0.0.0')
