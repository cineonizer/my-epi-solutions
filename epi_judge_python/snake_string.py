from test_framework import generic_test


def snake_string(s: str) -> str:
    res = []
    
    # top
    for i in range(1, len(s), 4):
        res.append(s[i])
    # mid
    for i in range(0, len(s), 2):
        res.append(s[i])
    # bottom
    for i in range(3, len(s), 4):
        res.append(s[i])
    return ''.join(res)
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
