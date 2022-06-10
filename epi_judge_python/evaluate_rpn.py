from test_framework import generic_test
import operator

def evaluate(expression: str) -> int:
    s = []
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: b - a,
        '*': lambda a, b: a * b,
        '/': lambda a, b: b // a
    }

    for c in expression.split(','):
        if c in operators:
            s.append(operators[c](s.pop(), s.pop()))
        else:
            s.append(int(c))
    return s[-1]


    # my solution (ugly with all the if statements)
    expression = expression.split(',')
    s = [] # stack
    for c in expression:
        if not c.isdigit():
            val1 = int(s.pop())
            val2 = int(s.pop())
            if c == '+':
                s.append(str(val1 + val2))
            if c == '-':
                s.append(str(val2 - val1))
            if c == '*':
                s.append(str(val1 * val2))
            if c == '/':
                s.append(str(val2 // val1))
        else:
            s.append(c)
    return int(s.pop())



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
