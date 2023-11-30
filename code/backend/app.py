from flask import Flask, make_response
from helper import example_function

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/")
def healthcheck():
    response = make_response('<p>Healthcheck Successful</p>')
    response.status_code = 200
    return response

@app.route("/example")
def example():
    result = example_function("Example Function Executed!!")

    response = make_response(result)
    response.status_code = 200
    return response
    


