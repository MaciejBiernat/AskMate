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
def get_question_info(cursor, question_id):
    cursor.execute("""
                        SELECT question.title, question.message, question.id FROM question
                        where question.id = %(question_id)s;
                               """, {'question_id': question_id})

    question_info = cursor.fetchall()
    return question_info


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