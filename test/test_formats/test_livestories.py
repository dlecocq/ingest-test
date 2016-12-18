'''Tests about the livestories data format.'''

import os

from ingest.formats.livestories import LiveStories, Row

from .. import BaseTest


class LiveStoriesTest(BaseTest):
    '''Tests about the livestories data format.'''

    def test_round_trip(self):
        '''Can round-trip records through a file.'''
        rows = [
            Row('place-1', '1', 'metric-1', 'value-1'),
            Row('place-2', '2', 'metric-2', 'value-2'),
            Row('place-3', '3', 'metric-3', 'value-3')
        ]
        with self.tmpdir() as directory:
            path = os.path.join(directory, 'example.livestories')
            with LiveStories.open(path, 'w+') as fout:
                fout.write(rows)

            with LiveStories.open(path) as fin:
                actual = list(fin.rows())

            self.assertEqual(rows, actual)
