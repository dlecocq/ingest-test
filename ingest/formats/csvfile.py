'''The CSV data format.'''

import csv
import itertools

from . import FormatBaseClass, Row


class Csvfile(FormatBaseClass):
    '''
    A file-like object for reading the CSV data format.

    It accepts a function for determining the place of a record given a row, as well as a
    function for determining the time of a record given a row.

    It then produces a value for each column in each row.
    '''

    def __init__(self, fobj, place_func, time_func):
        FormatBaseClass.__init__(self, fobj)
        self.reader = csv.reader(fobj)
        self.fieldnames = next(self.reader)
        self.place_func = place_func
        self.time_func = time_func

    def rows(self):
        '''Generator for all the rows in the file.'''
        for row in self.reader:
            place = self.place_func(row)
            time = self.time_func(row)
            for metric, value in itertools.izip(self.fieldnames, row):
                yield Row(place, time, metric, value)
