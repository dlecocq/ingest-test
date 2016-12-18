'''Tests about the util module.'''

from ingest import util
from ingest.formats import Row

from . import BaseTest


class UtilTest(BaseTest):
    '''Tests about the util module.'''

    def test_summed(self):
        '''Summed works as advertised.'''
        rows = [
            Row('place-1', '0', 'metric-1', '1'),
            Row('place-1', '0', 'metric-2', '1'),
            Row('place-1', '1', 'metric-1', '1'),
            Row('place-1', '1', 'metric-1', '3'),
            Row('place-2', '0', 'metric-1', '1'),
            Row('place-2', '0', 'metric-2', '1'),
            Row('place-2', '0', 'metric-1', '1')
        ]
        expected = [
            Row('place-1', '0', 'metric-1', '1'),
            Row('place-1', '0', 'metric-2', '1'),
            Row('place-1', '1', 'metric-1', '4'),
            Row('place-2', '0', 'metric-1', '2'),
            Row('place-2', '0', 'metric-2', '1')
        ]
        self.assertEqual(
            expected, sorted(util.summed(rows)))

    def test_summed_empty(self):
        '''Does not blow up when handed an empty iterable.'''
        self.assertEqual([], list(util.summed([])))
