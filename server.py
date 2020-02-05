from flask import Flask, render_template, request, redirect, url_for
from collections import OrderedDict
import connection
import data_manager
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def route_list():
    return render_template("index.html")


@app.route('/list')
def show_list_of_questions():
    list_of_questions = data_manager.get_questions()
    titles = ['ID', 'Submission Time', 'View Number', 'Vote Number', 'Title', 'Message', 'Image']

    return render_template('list.html', list_of_questions=list_of_questions, titles=titles)


@app.route('/question/<int:question_id>')
def show_question_info(question_id):
    question = data_manager.get_question_info(question_id)
    answers = data_manager.get_answer_info(question_id)

    return render_template('question.html', question=question, answers=answers)

@app.route('/question/<question_id>/new-answer', methods=["GET", "POST"])
def post_an_answer(question_id):
    new_answer = {}
    print('dupa')
    if request.method == "POST":
        new_answer["submission_time"] = datetime.now()
        new_answer['message'] = request.form['message']
        new_answer['image'] = 'img'
        new_answer['question_id'] = question_id

        return redirect(f'/question/{question_id}')
    return render_template("add-answer.html", question_id=question_id)


@app.route('/add-question', methods=["GET", "POST"])
def ask_question():
    new_question = {}
    titles = ["submission_time", "view_number", "vote_number", "title", "message", "image"]
    if request.method == "POST":
        new_question["submission_time"] = datetime.now()
        new_question["view_number"] = "0"
        new_question["vote_number"] = "0"
        new_question["title"] = request.form["title"]
        new_question["message"] = request.form["message"]
        new_question["image"] = "img"

        question_id = data_manager.add_question(new_question.items())
        return redirect(f'/question/{question_id}')

    return render_template("add-question.html")


#
#
# @app.route('/question/<question_id>/new-answer')
# def post_an_answer():
#


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )