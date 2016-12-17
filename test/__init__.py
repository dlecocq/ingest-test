'''All the tests for ingest.'''

import contextlib
import os
import shutil
import tempfile
import unittest

class BaseTest(unittest.TestCase):
    '''Base test class.'''

    @contextlib.contextmanager
    def tmpdir(self):
        '''Give a path to a temporary directory, deleting it after.'''
        directory = tempfile.mkdtemp()
        try:
            yield directory
        finally:
            shutil.rmtree(directory)
