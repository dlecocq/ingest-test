'''Various data formats.'''

import collections
import contextlib

# The Row "class"
Row = collections.namedtuple('Row', ['place', 'time', 'metric', 'value'])


class FormatBaseClass(object):
    '''Base class for all formats.'''

    @classmethod
    @contextlib.contextmanager
    def open(cls, path, mode='r', **kwargs):
        '''
        Open the file provided as this format. Additional kwargs are passed to the
        constructor.
        '''
        with contextlib.closing(cls(open(path, mode), **kwargs)) as fobj:
            yield fobj

    def __init__(self, fobj):
        self.fobj = fobj

    def close(self):
        '''Close this file.'''
        self.fobj.close()
