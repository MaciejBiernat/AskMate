import connection


@connection.connection_handler
def get_questions(cursor):
    cursor.execute("""
                        SELECT * FROM question;
                               """)
    questions = cursor.fetchall()
    return questions



