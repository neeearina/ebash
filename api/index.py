from data import db_session
from flask import Flask
from parsing import selenium_find
app = Flask(__name__)


@app.route('/')
def mission():
    return "EBASH"

def main():
    db_session.global_init("db/main_db.db")
    app.run()
    # selenium_find()


if __name__ == '__main__':
    main()
    app.run(port=5000, host='0.0.0.0')

