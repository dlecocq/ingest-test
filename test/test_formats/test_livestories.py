'''Tests about the livestories data format.'''

import os

from ingest.formats.livestories import LiveStories

from .. import BaseTest


class LiveStoriesTest(BaseTest):
    '''Tests about the livestories data format.'''

    def test_round_trip(self):
        '''Can round-trip records through a file.'''
        rows = [
            LiveStories.Row('place-1', '1', 'field-1', 'value-1'),
            LiveStories.Row('place-2', '2', 'field-2', 'value-2'),
            LiveStories.Row('place-3', '3', 'field-3', 'value-3')
        ]
        with self.tmpdir() as directory:
            path = os.path.join(directory, 'example.livestories')
            with LiveStories.open(path, 'w+') as fout:
                fout.write(rows)

            with LiveStories.open(path) as fin:
                actual = list(fin.rows())

            self.assertEqual(rows, actual)
