"""
.. module:: plot

This Python module plots blood pressure readings.

"""
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot(data):
    """ Plot a stream of blood pressure measurements.

    :data: iterator returning tuples in the form
           (datetime, systolic, diastolic).
    """
    times, systolic, diastolic = zip(*data)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.ylabel('mmHg')
    plt.title('blood pressure measurements')
    plt.gcf().autofmt_xdate()
    plt.plot(times, systolic)
    plt.plot(times, diastolic)
    plt.show()


if __name__ == '__main__':

    import os
    import sys

    dir = os.path.dirname(__file__)
    sys.path.insert(0, os.path.abspath(os.path.join(dir, '..')))

    from pressures.get_csv import get_csv

    if len(sys.argv) < 2:
        print('error: CSV file parameter required\n', file=sys.stderr)
        print('usage: plot filename.csv')
        # print('usage: plot filename.csv [ <start_date> [ <end_date> ]]',
        #       file=sys.stderr)
        sys.exit(9)

    plot(get_csv(sys.argv[1]))
    sys.exit(0)
