from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/1049b6f782550350db44")
    posts_json = response.json()["posts"]
    return render_template("index.html", posts=posts_json)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    response = requests.get("https://api.npoint.io/1049b6f782550350db44")
    result_post = {}
    for post in response.json()["posts"]:
        if post["id"] == post_id:
            result_post = post
    return render_template('post.html', post=result_post)


if __name__ == "__main__":
    app.run(debug=True)
