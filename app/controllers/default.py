from app import app
from flask import render_template


@app.route("/",defaults={"user":None})
def index(user):
    return render_template('index.html', user="Eduardo")