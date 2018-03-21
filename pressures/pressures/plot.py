"""
.. module:: plot

This Python module plots blood pressure readings.

"""
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy

window_len = 19


def moving_average(x, n=window_len):
    avgs = numpy.cumsum(numpy.array(x), dtype=float)
    avgs[n:] = avgs[n:] - avgs[:-n]
    return avgs[n-1:] / n


def plot(data, avgs=True, raw_data=False):
    """ Plot a stream of blood pressure measurements.

    :data: iterator returning tuples in the form
           (datetime, systolic, diastolic).
    :avgs: plot moving averages, if True.
    :raw_data: plot raw data, if True.
    """
    if not avgs and not raw_data:       # nothing to do?
        return
    times, systolic, diastolic = zip(*data)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.ylabel('mmHg')
    plt.gcf().autofmt_xdate()
    plt.axis([min(times), max(times), 0, max(systolic)])
    if raw_data:
        plt.title('blood pressure measurements')
        plt.plot(times, systolic, 'ro', label='systolic')
        plt.plot(times, diastolic, 'bs', label='diastolic')
        plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    if avgs:
        if not raw_data:
            plt.title('blood pressure averages')
        plt.plot(times[window_len-1:], moving_average(systolic), 'r', linewidth=4)
        plt.plot(times[window_len-1:], moving_average(diastolic), 'b', linewidth=4)
    plt.show()
