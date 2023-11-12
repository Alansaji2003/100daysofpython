import time
#
# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return "HELLO World"
#
# if __name__ == "__main__":
#     app.run()

#functions in python are first class objects that means they can be passed as arguments
##python decorators
# def decorator_function(function):
#     def wrapper_function():
#         function()
#     return wrapper_function()





#example
def delay_decorator(function):
    def wrapper():
        time.sleep(2)
        #Do something before
        function()
        function()
        #do something after
    return wrapper()


@delay_decorator
def say_hi():
    print("Hey")

@delay_decorator
def say_bye():
    print("Bye")

def lol():
    print("Looa")



say_hi()

