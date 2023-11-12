import random
from flask import Flask

app = Flask(__name__)

random_number = random.randint(0,10)

@app.route("/")
def index():
    return "<h1 style='text-align:center'>Guess a number between 0 and 9 and type in URL<h1/><img  src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWdhODU4a2ptMWEwcmZoam9sOXd0emp1N3plYWNyZHUxMHowdmltMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tsX3YMWYzDPjAARfeg/giphy.gif' style='padding-left:630px'>"


@app.route("/<int:number>")
def guess(number):
    if number == random_number:
        return "<h1 style='text-align:center'>Ahh you found me!<h1/><img  src='https://media.giphy.com/media/5wWf7HfZ0YYUzkdNYas/giphy.gif' style='padding-left:550px'>"
    elif number < random_number:
        return "<h1 style='text-align:center'>Too low bruh!<h1/><img  src='https://media.giphy.com/media/RVr9ZajlHNgbfweEWr/giphy.gif' style='padding-left:550px'>"
    else:
        return "<h1 style='text-align:center'>That shi high af<h1/><img  src='https://media.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif' style='padding-left:550px'>"


if __name__ == "__main__":
    app.run(debug=True)