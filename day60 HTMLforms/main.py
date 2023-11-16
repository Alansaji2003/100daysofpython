from flask import Flask, request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>name : {name}, password: {password}<h1/>"


if __name__ == "__main__":
    app.run()

