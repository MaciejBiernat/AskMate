import connection, datetime


def time_decoding(filename):

    unconverted_time_dicts = connection.reader_csv(filename)

    converted = []
    for item in unconverted_time_dicts:
        for k, value in item.items():
            if k == "submission_time":
                new_time = datetime.datetime.fromtimestamp(int(value))
                item.update({"submission_time": str(new_time)})
                converted.append(item)

    return converted

def generate_next_id(filename):
    old_data = connection.reader_csv(filename)
    max_id = 0
    for row in old_data:
        max_id += 1
    new_id = max_id
    return new_id
