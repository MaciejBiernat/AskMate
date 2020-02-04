from flask import Flask, render_template, request, redirect, url_for
from collections import OrderedDict
import connection
import data_manager

app = Flask(__name__)


@app.route('/')
def route_list():

    return render_template("index.html")


@app.route('/question')



@app.route('/question/<int:question_id>')



@app.route('/add-question', methods=["GET", "POST"])
def ask_question():


@app.route('/question/<question_id>/new-answer')
def post_an_answer():



if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )