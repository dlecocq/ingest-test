'''Tests about the crdc data format.'''

from cStringIO import StringIO

from ingest.formats.crdc import Crdc, Row

from .. import BaseTest


class CrdcTest(BaseTest):
    '''Tests about the crdc data format.'''

    def test_read(self):
        '''Can read records from the CSV.'''
        lines = [
            'LEAID,SCHID,SCH_PSENR_M,SCH_PSENR_F,SCH_PSENR_HI_M,SCH_PSENR_HI_F',
            '0100000,01705,100,92,12,16',
            '0100000,01862,51,50,8,-9',
            '0100001,01923,68,73,3,5',
            '0100001,01962,12,10,0,1'
        ]
        fobj = StringIO('\n'.join(lines))
        expected = [
            Row('0100000', '2013', 'SCH_PSENR_M', '151'),
            Row('0100000', '2013', 'SCH_PSENR_F', '142'),
            Row('0100000', '2013', 'SCH_PSENR', '293'),
            Row('0100000', '2013', 'SCH_PSENR_HI_M', '20'),
            Row('0100000', '2013', 'SCH_PSENR_HI_F', '16'),
            Row('0100000', '2013', 'SCH_PSENR_HI', '36'),
            Row('0100001', '2013', 'SCH_PSENR_M', '80'),
            Row('0100001', '2013', 'SCH_PSENR_F', '83'),
            Row('0100001', '2013', 'SCH_PSENR', '163'),
            Row('0100001', '2013', 'SCH_PSENR_HI_M', '3'),
            Row('0100001', '2013', 'SCH_PSENR_HI_F', '6'),
            Row('0100001', '2013', 'SCH_PSENR_HI', '9')
        ]

        actual = Crdc(fobj, '2013').rows()

        self.assertEqual(sorted(expected), sorted(actual))

    def test_field_order_independence(self):
        '''Can read records from the CSV no matter the order of the fields'''
        lines = [
            'SCHID,LEAID,SCH_PSENR_M,SCH_PSENR_F,SCH_PSENR_HI_M,SCH_PSENR_HI_F',
            '01705,0100000,100,92,12,16',
            '01862,0100000,51,50,8,-9',
            '01923,0100001,68,73,3,5',
            '01962,0100001,12,10,0,1'
        ]
        fobj = StringIO('\n'.join(lines))
        expected = [
            Row('0100000', '2013', 'SCH_PSENR_M', '151'),
            Row('0100000', '2013', 'SCH_PSENR_F', '142'),
            Row('0100000', '2013', 'SCH_PSENR', '293'),
            Row('0100000', '2013', 'SCH_PSENR_HI_M', '20'),
            Row('0100000', '2013', 'SCH_PSENR_HI_F', '16'),
            Row('0100000', '2013', 'SCH_PSENR_HI', '36'),
            Row('0100001', '2013', 'SCH_PSENR_M', '80'),
            Row('0100001', '2013', 'SCH_PSENR_F', '83'),
            Row('0100001', '2013', 'SCH_PSENR', '163'),
            Row('0100001', '2013', 'SCH_PSENR_HI_M', '3'),
            Row('0100001', '2013', 'SCH_PSENR_HI_F', '6'),
            Row('0100001', '2013', 'SCH_PSENR_HI', '9')
        ]

        actual = Crdc(fobj, '2013').rows()

        self.assertEqual(sorted(expected), sorted(actual))
