from re import L
from test_framework import generic_test
from test_framework.test_failure import TestFailure

import collections

class QueueWithMax:
    def __init__(self):
        self._q = collections.deque()
        self._d = collections.deque()

    def enqueue(self, x: int) -> None:
        while self._d and self._d[-1] < x:
            self._d.pop()
        self._q.append(x)
        self._d.append(x)

    def dequeue(self) -> int:
        res = self._q.popleft()
        if res == self._d[0]:
            self._d.popleft()
        return res    

    def max(self) -> int:
        return self._d[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
