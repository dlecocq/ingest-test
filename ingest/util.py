'''Utility functions.'''

from collections import defaultdict
import operator

from .formats import Row


def reducer(rows, reduce_function):
    '''
    Given an iterable of rows sorted by (place, time), yield
    reduce_function(place, time, metric, values) for the values from each metric with a
    maching (place, time). In map-reduce parliance, it's like conducting the reduce step
    with a key of (place, time, metric).
    '''
    values = defaultdict(list)
    iterator = iter(rows)
    try:
        row = next(iterator)
        current = (row.place, row.time)
        values[row.metric].append(row.value)
    except StopIteration:
        return

    for row in iterator:
        key = (row.place, row.time)
        if current != key:
            for metric, values in values.items():
                place, time = current
                yield reduce_function(place, time, metric, values)
            values = defaultdict(list)
            current = key

        values[row.metric].append(row.value)

    # Clear out all remaining values
    for metric, values in values.items():
        place, time = current
        yield reduce_function(place, time, metric, values)


def summed(rows):
    '''Reducer that sums the values of repeated metrics.'''
    def reduce_function(place, time, metric, values):
        '''Sum the values for this metric.'''
        return Row(place, time, metric, str(reduce(operator.add, map(int, values))))

    return reducer(rows, reduce_function)
