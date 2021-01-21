#! /usr/bin/python3
from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(error):
    _ = error
    return redirect('/')


if __name__ == '__main__':
    app.run()
