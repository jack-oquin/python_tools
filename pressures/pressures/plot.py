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
    plt.plot(times, systolic, 'ro')
    plt.plot(times, diastolic, 'bo')
    plt.show()
