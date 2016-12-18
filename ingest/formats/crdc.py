'''The Civil Rights Data Collection format.'''

import csv
import operator

from . import FormatBaseClass, Row
from ..util import summed


class Crdc(FormatBaseClass):
    '''
    A file-like object for reading the CRDC data format.
    '''

    def __init__(self, fobj, time):
        FormatBaseClass.__init__(self, fobj)
        self.reader = csv.reader(fobj)
        self.place_func = None
        self.time = time

        fieldnames = next(self.reader)

        # Figure out which columns we're going to take
        self.columns = []
        for index, column in enumerate(fieldnames):
            if column == 'LEAID':
                self.place_func = operator.itemgetter(index)
            if column.endswith('_M') or column.endswith('_F'):
                # The column itself
                self.columns.append((column, operator.itemgetter(index)))
                # The gender-removed column
                self.columns.append((column[:-2], operator.itemgetter(index)))

    def raw_rows(self):
        '''All the rows without any aggregation.'''
        for row in self.reader:
            for metric, getter in self.columns:
                # Negative values need to be treated as 0
                value = str(max(int(getter(row)), 0))
                yield Row(self.place_func(row), self.time, metric, value)

    def rows(self):
        '''Generator for all the rows in the file.'''
        return summed(self.raw_rows())
