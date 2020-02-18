from flask import Flask, render_template, request, redirect, url_for
from collections import OrderedDict
import connection
import data_manager
import bcrypt
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def route_list():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    register_form = {}
    if request.method == 'POST':
        if request.form['password'] == request.form['repeat password']:
            register_form['user_name'] = request.form['user_name']
            register_form['name'] = request.form['name']
            register_form['email'] = request.form['email']
            register_form['password'] = request.form['password']
            register_message = data_manager.check_user(register_form)

        else:
            return render_template("register.html", pass_message='passwords are not the same')
        return render_template("register.html", register_message=register_message)

    return render_template("register.html")


@app.route('/list')
def show_list_of_questions():
    list_of_questions = data_manager.get_questions()
    titles = ['ID', 'Submission Time', 'View Number', 'Vote Number', 'Title']

    return render_template('list.html', list_of_questions=list_of_questions, titles=titles)


@app.route('/question/<int:question_id>')
def show_question_info(question_id):
    question = data_manager.get_question_info(question_id)
    answers = data_manager.get_answer_info(question_id)

    return render_template('question.html', question=question, answers=answers)

@app.route('/question/<question_id>/new-answer', methods=["GET", "POST"])
def post_an_answer(question_id):
    new_answer = {}
    if request.method == "POST":
        new_answer["submission_time"] = datetime.now()
        new_answer['message'] = request.form['message']
        new_answer['image'] = 'img'
        new_answer['question_id'] = question_id

        data_manager.add_answer_to_db(new_answer.items())

        return redirect(f'/question/{question_id}')
    # wykorzystac URL_FOR
    return render_template("add-answer.html", question_id=question_id)


@app.route('/add-question', methods=["GET", "POST"])
def ask_question():
    header = "Ask a question"
    new_question = {}
    titles = ["submission_time", "view_number", "vote_number", "title", "message", "image"]
    if request.method == "POST":
        new_question["submission_time"] = datetime.now()
        new_question["view_number"] = "0"
        new_question["vote_number"] = "0"
        new_question["title"] = request.form["title"]
        new_question["message"] = request.form["message"]
        new_question["image"] = "img"
# DOCTESTY, TEST DRIVEN DEV
        question_id = data_manager.add_question(new_question.items())
        return redirect(f'/question/{question_id}')

    return render_template("add-question.html", header=header)


@app.route('/search')
def search_result():
    phrase = request.args.get('q')
    list_of_questions = data_manager.search_questions(phrase)
    titles = ['ID', 'Question title']

    return render_template('list.html', phrase=phrase, list_of_questions=list_of_questions, titles=titles)


@app.route('/question/<question_id>/delete endpoint')
def delete(question_id):
    data_manager.delete_question(question_id)
    return redirect('/list')


@app.route('/question/<question_id>/edit page', methods=["GET", "POST"])
def edit(question_id):
    header = "Edit question"
    question = data_manager.get_question_info(question_id)
    old_title = question[0]['title']
    old_message = question[0]['message']
    if request.method == "POST":
        new_submission_time = datetime.now()
        new_title = request.form["title"]
        new_message = request.form["message"]
        data_manager.edit_question(question_id, new_submission_time, new_title, new_message)

        return redirect(f'/question/{question_id}')
    return render_template('add-question.html', old_message=old_message, old_title=old_title, header=header)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
