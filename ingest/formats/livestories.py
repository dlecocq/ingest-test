'''The LiveStories data format.'''

from . import FormatBaseClass, Row


class LiveStories(FormatBaseClass):
    '''A file-like object for interacting with the livestories data format.'''

    field_seperator = '\t'
    record_seperator = '\n'

    def rows(self):
        '''Generator for all the rows in the file.'''
        for line in self.fobj:
            yield Row(*line.strip(self.record_seperator).split(self.field_seperator))

    def write(self, rows):
        '''Write the iterable of rows to this file.'''
        # TODO(dan): this currently doesn't do any type checking on the row, but it is
        # assumed to be a Row namedtuple
        for row in rows:
            self.fobj.write(self.field_seperator.join(row))
            self.fobj.write(self.record_seperator)
