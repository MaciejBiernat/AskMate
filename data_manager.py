import connection, datetime


def time_decoding(filename):

    unconverted_time_dicts = connection.reader_csv(filename)
    #'/home/ubuntu/codecool/Web/TW_Projects/AskMate1/question.csv'
    #all_answers = connection.reader_csv('/home/ubuntu/codecool/Web/TW_Projects/AskMate1/answer.csv')

    for item in unconverted_time_dicts:
        for k, value in item.items():
            if k == "submission_time":
                new_time = datetime.datetime.fromtimestamp(int(value))
                item.update({"submission_time":str(new_time)})

    converted_time_dicts = unconverted_time_dicts

    return converted_time_dicts
