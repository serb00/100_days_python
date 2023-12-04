from flask import Flask
app = Flask(__name__)


def is_authetnicated(func):
    def wrapper(*args):
        user: User = args[0]
        title = args[1]
        if user.is_logged_in:
            return func(user, title)
        else:
            return "You need to be logged in to perform this action"
    return wrapper


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

    @is_authetnicated
    def create_post(self, title):
        return f"User {self.name} created a post with title {title}"


def make_bold(func):
    def wrapper():
        result = func()
        return f"<b>{result}</b>"
    return wrapper


def make_emphasize(func):
    def wrapper():
        result = func()
        return f"<em>{result}</em>"
    return wrapper


def make_underline(func):
    def wrapper():
        result = func()
        return f"<u>{result}</u>"
    return wrapper


@app.route('/<is_logged_in>')
def index(is_logged_in):
    user = User("Serb")
    user.is_logged_in = bool(True if is_logged_in == "1" else False)
    return user.create_post("New post")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1234, debug=True)
