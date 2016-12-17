'''The LiveStories data format.'''

import contextlib
from collections import namedtuple


class LiveStories(object):
    '''A file-like object for interacting with the livestories data format.'''

    Row = namedtuple('Row', ['location', 'time', 'name', 'value'])

    field_seperator = '\t'
    record_seperator = '\n'

    @classmethod
    @contextlib.contextmanager
    def open(cls, path, mode='r'):
        '''Open the file provided as this format.'''
        with contextlib.closing(cls(open(path, mode))) as fobj:
            yield fobj

    def __init__(self, fobj):
        self.fobj = fobj

    def close(self):
        '''Close this file.'''
        self.fobj.close()

    def rows(self):
        '''Generator for all the rows in the file.'''
        for line in self.fobj:
            yield self.Row(*line.strip(self.record_seperator).split(self.field_seperator))

    def write(self, rows):
        '''Write the iterable of rows to this file.'''
        # TODO(dan): this currently doesn't do any type checking on the row, but it is
        # assumed to be a Row namedtuple
        for row in rows:
            self.fobj.write(self.field_seperator.join(row))
            self.fobj.write(self.record_seperator)
