from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    # my solution
    has_leading_slash = True if path[0] == '/' else False
    stack = []
    for c in path.strip('/').split('/'):
        if c == '..' and stack and stack[-1].isalnum():
            stack.pop()
        elif c != '.' and c != '':
            stack.append(c)
    return '/' + '/'.join(stack) if has_leading_slash else '/'.join(stack)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
