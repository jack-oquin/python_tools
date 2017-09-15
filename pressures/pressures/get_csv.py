"""
.. module:: get_csv

This Python module reads a CSV file containing blood pressure data.

"""
import csv
from dateutil.parser import parse

def format_pressures(row):
    """ Returns a tuple for each row in the CSV file.

    :param row: four elements: date, time, systolic, diastolic.

    :returns:  tuple containing: (datetime, systolic, diastolic).
    """
    time = parse(row[0] + ' ' + row[1], ignoretz=True)
    systolic = int(row[2])
    diastolic = int(row[3])
    return (time, systolic, diastolic)

def get_csv(filename):
    """ Returns an iterator for the rows of the named CSV file. """
    for row in csv.reader(open(filename)):
        yield format_pressures(row)
