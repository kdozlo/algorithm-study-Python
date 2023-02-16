import sys
from bisect import bisect_left, bisect_right
input = lambda: sys.stdin.readline().rstrip()


def count_by_range(arry, left_value, right_value):
    right_index = bisect_right(arry, right_value)
    left_index = bisect_left(arry, left_value)

    return right_index - left_index

n, x = map(int, input().split())

arry = list(map(int, input().split()))


result = count_by_range(arry, x, x)

if result == 0:
    print(-1)
else : 
    print(result)