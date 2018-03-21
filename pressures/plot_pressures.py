#! /usr/bin/env python3

"""
.. module:: plot_pressures.py

This module is an executable Python script for ploting blood pressure readings.

"""
import sys
from optparse import OptionParser
from pressures.get_csv import get_csv
from pressures.plot import plot


if __name__ == '__main__':

    parser = OptionParser(usage='usage: %prog [options] FILENAME.CSV')
    parser.add_option("-a", "--no-avgs",
                      action="store_false", dest="avgs", default=True,
                      help="do not plot moving averages")
    parser.add_option("-d", "--data",
                      action="store_true", dest="raw_data", default=False,
                      help="plot raw data")
    (options, args) = parser.parse_args()

    if len(args) != 1:
        print('error: a single CSV file name parameter is required\n', file=sys.stderr)
        parser.print_help()
        sys.exit(9)

    plot(get_csv(args[0]), avgs=options.avgs, raw_data=options.raw_data)
    sys.exit(0)
