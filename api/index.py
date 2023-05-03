from data import db_session
from flask import Flask
from parsing import selenium_find_category

app = Flask(__name__)


@app.route('/')
def mission():
    return "EBASH"


def main():
    db_session.global_init("db/main_db.db")
    # selenium_find_category()  # чтобы загрузить категории профессий в бд
    app.run()


if __name__ == '__main__':
    main()
    app.run(port=5000, host='0.0.0.0')
