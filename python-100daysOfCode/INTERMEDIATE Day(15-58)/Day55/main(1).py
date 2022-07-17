from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"<p><b>Hello, {name}!, you are {number} years old.</b></p>"

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "bye!"

if __name__ == "__main__":
    app.run(debug=True)
