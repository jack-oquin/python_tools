#! /usr/bin/env python3

"""
.. module:: plot_pressures.py

This module is an executable Python script for ploting blood pressure readings.

"""
import sys
from pressures.get_csv import get_csv
from pressures.plot import plot


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('error: CSV file parameter required\n', file=sys.stderr)
        print('usage: plot filename.csv')
        # print('usage: plot filename.csv [ <start_date> [ <end_date> ]]',
        #       file=sys.stderr)
        sys.exit(9)

    plot(get_csv(sys.argv[1]))
    sys.exit(0)
