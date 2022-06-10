from test_framework import generic_test


def look_and_say(n: int) -> str:
    def next_number(s):
        res = []
        repeat_count = 0
        left = 0
        for right in range(len(s)):
            if s[left] == s[right]:
                repeat_count += 1
            else:
                res.append(str(repeat_count) + s[left])
                left = right
                repeat_count = 1
        res.append(str(repeat_count) + s[left])
        return ''.join(res)
        
    s = '1'
    for _ in range(1, n):
        s = next_number(s)
    return s

    # my original solution but made the mistake of using O(n*2^n) space complexity as well because of the lookup nested array
    # it is not necessary to save the older string values just need the adjacent previous string (not all the previous ones)
    
    # lookup = [['']] + [['1']] + [[] for _ in range(n - 1)]
    # for i in range(2, len(lookup)):
    #     prev_lookup = lookup[i - 1]
    #     repeat_count = 0
    #     left = 0
    #     for right in range(len(prev_lookup)):
    #         if prev_lookup[left] == prev_lookup[right]:
    #             repeat_count += 1
    #         else:
    #             lookup[i].append(str(repeat_count))
    #             lookup[i].append(prev_lookup[left])
    #             left = right
    #             repeat_count = 1
    #     lookup[i].append(str(repeat_count))
    #     lookup[i].append(prev_lookup[left])
    # return ''.join(lookup[-1])



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
