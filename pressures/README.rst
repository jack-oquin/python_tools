pressures
=========

A Python3 package for reading and displaying blood pressure
measurements.

install
-------

From the main source directory, run::

  sudo python3 setup.py install

how to plot data
----------------

Open the Google Drive sheet in a browser.

Select ``File>Download as>Comma-separated values (.csv current sheet)``

Run the ``plot_pressures.py`` command on the downloaded file::

  plot_pressures.py ~/Downloads/<file name>

In the plot window, select save plot and provide a file name.

command line
------------

  Usage:
    plot_pressures.py [options] FILENAME.CSV

  Options:
    -h, --help     show this help message and exit
    -a, --no-avgs  do not plot moving averages
    -d, --data     plot raw data
