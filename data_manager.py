import connection


@connection.connection_handler
def get_questions(cursor):
    cursor.execute("""
                        SELECT * FROM question;
                               """)
    questions = cursor.fetchall()
    return questions

@connection.connection_handler
def add_question(cursor, new_question):
    placeholders = ', '.join(['%s'] * len(new_question))
    columns = ', '.join([x[0] for x in new_question])
    sql = "INSERT INTO %s ( %s ) VALUES ( %s ) RETURNING * ;" % ('question', columns, placeholders)

    cursor.execute(sql, [y[1] for y in new_question])
    rows = cursor.fetchall()
    id = max([row['id'] for row in rows])
    return id


@connection.connection_handler
def edit_question(cursor, question_id, new_submission_time, new_title, new_message):
    cursor.execute(""" 
                        UPDATE question 
                        SET submission_time = %(new_submission_time)s, title = %(new_title)s, message = %(new_message)s
                        WHERE question.id = %(question_id)s;
                         """,
                   {'new_submission_time': new_submission_time, 'new_title': new_title, 'new_message': new_message,
                    'question_id': question_id})


@connection.connection_handler
def get_question_info(cursor, question_id):
    cursor.execute("""
                        SELECT question.title, question.message, question.id FROM question
                        where question.id = %(question_id)s;
                               """, {'question_id': question_id})

    question_info = cursor.fetchall()
    return question_info


@connection.connection_handler
def delete_question(cursor, question_id):
    cursor.execute("""
                        DELETE FROM answer
                        WHERE answer.question_id = %(question_id)s;
                        DELETE FROM question
                        WHERE question.id = %(question_id)s
           
                               """, {'question_id': question_id})


@connection.connection_handler
def get_answer_info(cursor, question_id):
    cursor.execute("""
                        SELECT answer.message FROM answer
                        where answer.question_id = %(question_id)s;
                               """, {'question_id': question_id})

    answer_info = cursor.fetchall()
    return answer_info

@connection.connection_handler
def add_answer_to_db(cursor, new_answer):
    placeholders = ', '.join(['%s'] * len(new_answer))
    columns = ', '.join([x[0] for x in new_answer])
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('answer', columns, placeholders)

    cursor.execute(sql, [y[1] for y in new_answer])

@connection.connection_handler
def search_questions(cursor, phrase):
    # sql = '''SELECT id FROM question WHERE message LIKE '%%%s%%'
    # UNION
    # SELECT question_id FROM answer WHERE message LIKE '%%%s%%';''' % (phrase, phrase)
    sql = '''select distinct question.id, question.title, question.message from question
            left join answer on answer.question_id = question.id
            WHERE question.message LIKE '%%%s%%' OR question.title LIKE '%%%s%%' OR answer.message LIKE '%%%s%%' 
            ORDER BY question.id;''' % (phrase, phrase, phrase)
    cursor.execute(sql)
    questions = cursor.fetchall()

    return questions

