import csv
import os


def reader_csv(filename):
    dictionaries = csv.DictReader(open(filename))
    return dictionaries

def writer_csv(filename, fieldnames, new_data):
    with open(filename, 'a') as my_file:
        writer = csv.DictWriter(my_file, fieldnames=fieldnames)
        writer.writerow(new_data)

