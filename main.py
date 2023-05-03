from data import db_session
from flask import Flask

app = Flask(__name__)


@app.route('/ebash')
def mission():
    return "EBASH"


def main():
    db_session.global_init("db/main_db.db")
    app.run()


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')