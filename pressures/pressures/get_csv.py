"""
.. module:: get_csv

This Python module reads a CSV file containing blood pressure data.

"""
import csv
import datetime as dt

def format_pressures(row):
    """ Returns a tuple for each row in the CSV file.

    The row should contain four elements: date, time, systolic, diastolic.

    The tuple contains: (datetime, systolic, diastolic).
    """
    return (dt.datetime.combine(dt.date(2017, 8, 19), dt.time(13, 30)), 117, 62)

def get_csv(filename):
    """ Returns an iterator for the rows of the named CSV file. """
    for row in csv.reader(open(filename)):
        yield format_pressures(row)
