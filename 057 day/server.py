from flask import Flask, render_template
from random import randint
import datetime as dt
import requests

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        "body_content": "Hello from world!",
        "rand_int": randint(1, 10),
        "cur_year": dt.datetime.now().year
    }
    return render_template('index.html', **context)


@app.route('/guess/<name>')
def func_name(name):
    response = requests.get(f"https://api.agify.io/?name={name}")
    response.raise_for_status()
    age = response.json()["age"]
    response = requests.get(f"https://api.genderize.io/?name={name}")
    response.raise_for_status()
    gender = response.json()["gender"]
    context = {
        "name": name,
        "age": age,
        "gender": gender,
        "cur_year": dt.datetime.now().year
    }
    return render_template('index.html', **context)


@app.route('/blogs')
def blogs():
    response = requests.get("https://api.npoint.io/1049b6f782550350db44")
    all_posts = response.json()["posts"]
    return render_template('blogs.html', posts=all_posts)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1234, debug=True)
