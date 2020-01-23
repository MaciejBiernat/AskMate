from flask import Flask, render_template, request, redirect, url_for
from collections import OrderedDict
import connection
import data_manager

app = Flask(__name__)


@app.route('/')
def route_list():

    return render_template("index.html")


@app.route('/question')
def list_questions():
    '''Implement the /list page that displays all questions.

    The page is available under /list
    Load and display the data from question.csv
    Sort the questions by the latest question on top
    '''

    titles = ['ID', 'Submission Time', 'View Number', 'Vote Number', 'Title']
    all_questions = data_manager.time_decoding('question.csv')
    for question in all_questions:
        print(question)
    return render_template("list.html", all_questions=all_questions, titles=titles)


@app.route('/question/<int:question_id>')
def display_question(question_id):
    '''Create the /question/<question_id> page that displays a question and the answers for it.

    The page is available under /question/<question_id>
    There are links to the question pages from the list page
    The page displays the question title and message
    The page displays all the answers to a question'''
    all_questions = data_manager.time_decoding('question.csv')
    all_answers = data_manager.time_decoding('answer.csv')

    for row in all_questions:
        if row['id'] == str(question_id):
            question = row
    answers = []
    for row in all_answers:
        if row['id'] == str(question_id):
            answers.append(row)

    return render_template('question.html', question=question, answers=answers)

@app.route('/add-question', methods=["GET", "POST"])
def ask_question():
    '''
    Implement a form that allows you to add a question.

    There is an /add-question page with a form
    The page is linked from the list page
    There is a POST form with at least title and message fields
    After submitting, you are redirected to "Display a question" page of this new question
    :return:
    '''
    new_question = {}
    titles = ["id", "submission_time", "view_number", "vote_number", "title", "message", "image"]
    if request.method == "POST":
        question_id = data_manager.generate_next_id("question.csv")
        new_question["id"] = question_id
        new_question["submission_time"] = "1493068124"
        new_question["view_number"] = "view number"
        new_question["vote_number"] = "vote_number"
        new_question["title"] = request.form["title"]
        new_question["message"] = request.form["message"]
        new_question["image"] = "img"
        # dodać zapisywanie z potrzebnymi innymi kolumnami
        # ewentualnie dodać jakoś ten image
        connection.writer_csv("question.csv", titles, new_question)
        return redirect(f'/question/{question_id}')
    return render_template("add-question.html")


@app.route('/question/<question_id>/new-answer')
def post_an_answer():
    '''
    Implement posting a new answer.

    The page URL is /question/<question_id>/new-answer
    The question detail page links to this page
    The page has a POST form with a form field called message
    Posting an answer redirects you back to the question detail page, and the new answer is there
    :return:
    '''

    return render_template('question.html')

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )