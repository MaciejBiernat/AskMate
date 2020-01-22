from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
def route_list():

    return render_template('index.html')


@app.route('/list')
def list_questions():
    '''Implement the /list page that displays all questions.

    The page is available under /list
    Load and display the data from question.csv
    Sort the questions by the latest question on top
    '''
    return render_template('list.html')


@app.route('/queston/<question_id>')
def display_question():
    '''Create the /question/<question_id> page that displays a question and the answers for it.

    The page is available under /question/<question_id>
    There are links to the question pages from the list page
    The page displays the question title and message
    The page displays all the answers to a question'''

    return render_template('question.html')

@app.route('/add-question')
def ask_question():
    '''
    Implement a form that allows you to add a question.

    There is an /add-question page with a form
    The page is linked from the list page
    There is a POST form with at least title and message fields
    After submitting, you are redirected to "Display a question" page of this new question
    :return:
    '''

    return render_template('add_question.html')

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