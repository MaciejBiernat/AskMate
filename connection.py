import csv
import os


#
# def get_all_user_story():
#     user_stories = csv.DictReader(open("data.csv"))
#     return user_stories
#
# def save_stories(requests):
#
#     with open('data.csv', 'a') as my_file:
#         writer = csv.DictWriter(my_file, fieldnames=DATA_HEADER)
#         writer.writerow(requests)
#     return []
#
# def generate_id():
#     previous_data = get_all_user_story()
#     max_id = 0
#     for row in previous_data:
#         max_id += 1
#     return max_id
