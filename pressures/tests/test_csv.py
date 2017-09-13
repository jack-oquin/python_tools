from unittest import TestCase

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pressures.get_csv import *

class TestCsv(TestCase):

    def test_small_csv(self):
        for entry in get_csv('./small_test.csv'):
            print(entry)

