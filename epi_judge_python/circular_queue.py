from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self._head = self._tail = self._size = 0
        self._capacity = capacity
        self._da = [None] * capacity

    def enqueue(self, x: int) -> None:
        # check if the dynamic array needs resizing
        if self._size == self._capacity:
            # reorder the dynamic array so that the elements are in order before upsizing
            self._da = self._da[self._head:] + self._da[:self._head]

            self._head, self._tail = 0, self._size
            self._da += ([None] * (self._capacity))
            self._capacity = len(self._da)
        
        # the element must be enqueued first before incrementing because the tail starts at 0
        self._da[self._tail] = x
        self._tail = (self._tail + 1) % self._capacity
        self._size += 1
        return

    def dequeue(self) -> int:
        res = self._da[self._head]
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return res

    def size(self) -> int:
        return self._size


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
