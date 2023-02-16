import sys
input = lambda:sys.stdin.readline().rstrip()

def count_by_value(arry, x):
    n = len(arry)

    left_index = left(arry, x, 0, n-1)

    if left_index == None:
        return 0

    right_index = right(arry, x, 0, n-1)

    return right_index - left_index + 1

def left(arry, x, start, end):
    
    if start > end:
        return None
    
    mid = (start + end) // 2

    if (mid == 0 or x > arry[mid - 1]) and arry[mid] == x:
        return mid
    elif arry[mid] >= x:
        return left(arry, x, start, mid - 1)
    elif arry[mid] < x:
        return left(arry, x, mid + 1, end)

def right(arry, x, start, end):

    if start > end:
        return None
    
    mid = (start + end) // 2

    if (mid == n - 1 or arry[mid + 1] > x) and arry[mid] == x:
        return mid
    elif arry[mid] > x:
        return right(arry, x, start, mid - 1)
    elif arry[mid] <= x:
        return right(arry, x, mid + 1, end)


n, x = map(int, input().split())
arry = list(map(int, input().split()))

count = count_by_value(arry, x)

if count == 0:
    print(-1)
else:
    print(count)
