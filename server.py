from flask import Flask, render_template, request, redirect, url_for
from collections import OrderedDict
import connection
import data_manager
import os

app = Flask(__name__)

print(os.getcwd())

@app.route('/')
def route_list():

    return render_template("index.html")


@app.route('/list')
def list_questions():
    '''Implement the /list page that displays all questions.

    The page is available under /list
    Load and display the data from question.csv
    Sort the questions by the latest question on top
    '''

    titles = ['ID', 'Submission Time', 'View Number', 'Vote Number', 'Title', 'Message', 'Image']
    all_questions = data_manager.time_decoding('question.csv')

    return render_template("list.html", all_questions=all_questions, titles=titles)


@app.route('/queston/<question_id>')
def display_question():
    '''Create the /question/<question_id> page that displays a question and the answers for it.

    The page is available under /question/<question_id>
    There are links to the question pages from the list page
    The page displays the question title and message
    The page displays all the answers to a question'''

    return render_template('question.html')

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
    if request.method == "POST":
        new_question["title"] = request.form["title"]
        new_question["message"] = request.form["message"]
        # dodać zapisywanie z potrzebnymi innymi kolumnami
        # ewentualnie dodać jakoś ten image
    return render_template('add-question.html')

@app.route('/queston/<question_id>/new-answer')
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