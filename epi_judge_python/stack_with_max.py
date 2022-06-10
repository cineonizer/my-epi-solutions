from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections

class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'cached_max'))
    
    def __init__(self) -> None:
        # O(n) space complexity
        self._items: List[Stack.ElementWithCachedMax] = []

    def empty(self) -> bool:
        # O(1) time complexity
        return len(self._items) == 0

    def max(self) -> int:
        # O(1) time complexity
        return self._items[-1].cached_max

    def pop(self) -> int:
        # O(1) amortized time complexity
        return self._items.pop().element

    def push(self, x: int) -> None:
        # O(1) amortized time complexity
        self._items.append(
            self.ElementWithCachedMax(x, x if self.empty() else max(self.max(), x))
        )

    """
    def __init__(self) -> None:
        # O(n) space complexity
        self._items = []

    def empty(self) -> bool:
        # O(1) time complexity
        return len(self.items) == 0

    def max(self) -> int:
        # O(n) time complexity
        max_val = self.items[0]
        for item in self.items:
            max_val = max(max_val, item)
        return max_val

    def pop(self) -> int:
        # O(1) amortized time complexity
        return self.items.pop()

    def push(self, x: int) -> None:
        # O(1) amortized time complexity
        self.items.append(x)
    """

        


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
