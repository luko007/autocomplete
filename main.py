import redis
from flask import Flask

app = Flask(__name__)


@app.route("/add")
def add():
    pass


@app.route("/suggest")
def suggest():
    pass
