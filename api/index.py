from data import db_session
from flask import Flask
#a
app = Flask(__name__)


@app.route('/')
def mission():
    return "EBASH"



