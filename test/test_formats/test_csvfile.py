'''Tests about the csvfile data format.'''

from cStringIO import StringIO
import operator

from ingest.formats.csvfile import Csvfile, Row

from .. import BaseTest


class CsvfileTest(BaseTest):
    '''Tests about the csv data format.'''

    def test_read(self):
        '''Can read records from a CSV.'''
        lines = [
            'place,time,metric-1,metric-2,metric-3',
            'Seattle,0,3.14,5.2,blue',
            'Chicago,0,2.71,6.3,red',
            'Denver,2,15,-1,green'
        ]
        fobj = StringIO('\n'.join(lines))
        expected = [
            Row('Seattle', '0', 'place', 'Seattle'),
            Row('Seattle', '0', 'time', '0'),
            Row('Seattle', '0', 'metric-1', '3.14'),
            Row('Seattle', '0', 'metric-2', '5.2'),
            Row('Seattle', '0', 'metric-3', 'blue'),
            Row('Chicago', '0', 'place', 'Chicago'),
            Row('Chicago', '0', 'time', '0'),
            Row('Chicago', '0', 'metric-1', '2.71'),
            Row('Chicago', '0', 'metric-2', '6.3'),
            Row('Chicago', '0', 'metric-3', 'red'),
            Row('Denver', '2', 'place', 'Denver'),
            Row('Denver', '2', 'time', '2'),
            Row('Denver', '2', 'metric-1', '15'),
            Row('Denver', '2', 'metric-2', '-1'),
            Row('Denver', '2', 'metric-3', 'green'),
        ]

        # In this example, the place is the first column, time is the second
        place_func = operator.itemgetter(0)
        time_func = operator.itemgetter(1)

        actual = list(Csvfile(fobj, place_func, time_func).rows())

        self.assertEqual(expected, actual)
