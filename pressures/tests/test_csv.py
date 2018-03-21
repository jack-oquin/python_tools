from unittest import TestCase

import os
import sys
import datetime as dt
from pressures.get_csv import get_csv

dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(dir, '..')))


def make_time(yr, mo, day, hr, min):
    return dt.datetime.combine(dt.date(yr, mo, day), dt.time(hr, min))


class TestCsv(TestCase):

    def test_small_csv(self):
        iter = get_csv(os.path.join(dir, 'small_test.csv'))
        self.assertEqual(next(iter), (make_time(2017, 8, 19, 13, 30), 117, 62))
        next(iter)
        next(iter)
        next(iter)
        self.assertEqual(next(iter), (make_time(2017, 8, 21, 9, 45), 156, 86))
        next(iter)
        next(iter)
        next(iter)
        self.assertEqual(next(iter), (make_time(2017, 8, 23, 23, 50), 145, 76))
        next(iter)
        next(iter)
        next(iter)
        self.assertEqual(next(iter), (make_time(2017, 8, 25, 16, 20), 170, 100))
        next(iter)
        next(iter)
        next(iter)
        self.assertEqual(next(iter), (make_time(2017, 8, 28, 9, 45), 144, 82))
        self.assertRaises(StopIteration, next, iter)
