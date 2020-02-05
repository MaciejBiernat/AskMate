from flask import Flask, render_template, request, redirect, url_for
from collections import OrderedDict
import connection
import data_manager

app = Flask(__name__)


@app.route('/')
def route_list():

    return render_template("index.html")

@app.route('/list')
def show_list_of_questions():
    list_of_questions = data_manager.get_questions()
    titles = ['ID', 'Submission Time', 'View Number', 'Vote Number', 'Title', 'Message', 'Image']

    return render_template('list.html', list_of_questions=list_of_questions, titles=titles)


#
# @app.route('/question')
#
#
#
# @app.route('/question/<int:question_id>')
#
#
#
@app.route('/add-question', methods=["GET", "POST"])
def ask_question():
    new_question = {}
    titles = ["submission_time", "view_number", "vote_number", "title", "message", "image"]
    if request.method == "POST":
        # question_id = data_manager.generate_next_id("question.csv")
        # new_question["id"] = question_id
        new_question["submission_time"] = "2017-05-01 10:41:00.000000"
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