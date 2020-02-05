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
    sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('question', columns, placeholders)

    cursor.execute(sql, [y[1] for y in new_question])
    id = cursor.lastrowid
    return id
