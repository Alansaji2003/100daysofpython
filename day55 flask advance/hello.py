from flask import Flask

app = Flask(__name__)


# making custom decorators
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


@app.route('/')
def helloworld():
    return "hello World!"


@app.route('/bye')
@make_bold
def bye():
    return "Bye"


# using variables
@app.route("/username/<name>")
def greet(name):
    return f"<h1>Hello there {name}<h1/>"


@app.route("/Age/<int:age>")
def age(age):
    return f"<b>You are {age} years old<b/>"


# See debug = True to automatically start server on change when ctrl+s
if __name__ == "__main__":
    app.run(debug=True)
