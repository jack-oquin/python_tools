pressures
=========

A Python3 package for reading and displaying blood pressure
measurements.

install
-------

From the main source directory, run::

  sudo python3 setup.py install

usage
-----

Open the Google Drive sheet in a browser.

Select ``File``>``Download as``>``Comma-separated values (.csv current sheet)``

Run this command on the downloaded file::

  plot_pressures.py ~Downloads/<file name>

In the plot window, select save plot and provide a file name.
