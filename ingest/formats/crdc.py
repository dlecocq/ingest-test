'''The Civil Rights Data Collection format.'''

import operator

from .csvfile import Csvfile, Row
from ..util import summed


class Crdc(Csvfile):
    '''
    A file-like object for reading the CRDC data format.
    '''

    def __init__(self, fobj, time):
        def time_func(_):
            '''The time is the same for all records in a file.'''
            return time

        Csvfile.__init__(self, fobj, operator.itemgetter(0), time_func)

    def raw_rows(self):
        '''All the rows without any aggregation.'''
        for row in Csvfile.rows(self):
            # Only yield rows with the metric ending in _M or _F
            if row.metric.endswith('_M') or row.metric.endswith('_F'):
                # Negative values need to be treated as 0
                value = str(max(int(row.value), 0))
                yield row._replace(value=value)
                # Also yield a row for this metric with the gender removed
                yield Row(row.place, row.time, row.metric[:-2], value)


    def rows(self):
        '''Generator for all the rows in the file.'''
        return summed(self.raw_rows())
