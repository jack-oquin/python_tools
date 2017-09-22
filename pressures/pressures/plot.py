"""
.. module:: plot

This Python module plots blood pressure readings.

"""
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy

window_len = 29

def moving_average(x, n=window_len):
    avgs = numpy.cumsum(numpy.array(x), dtype=float)
    avgs[n:] = avgs[n:] - avgs[:-n]
    return avgs[n-1:] / n

def plot(data):
    """ Plot a stream of blood pressure measurements.

    :data: iterator returning tuples in the form
           (datetime, systolic, diastolic).
    """
    times, systolic, diastolic = zip(*data)
    s_avg = moving_average(systolic)
    d_avg = moving_average(diastolic)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.ylabel('mmHg')
    plt.title('blood pressure measurements')
    plt.gcf().autofmt_xdate()
    plt.axis([min(times), max(times), 0, max(systolic)])
    plt.plot(times, systolic, 'ro', label='systolic')
    plt.plot(times[window_len-1:], s_avg, 'r', linewidth=4)
    plt.plot(times, diastolic, 'bs', label='diastolic')
    plt.plot(times[window_len-1:], d_avg, 'b', linewidth=4)
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.show()
