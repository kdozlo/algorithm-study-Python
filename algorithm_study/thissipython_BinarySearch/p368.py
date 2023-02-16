import sys
input = lambda:sys.stdin.readline().rstrip()

def binary_search(arry, start, end):

    if start > end:
        return -1

    mid = (start + end) // 2

    if arry[mid] == mid:
        return mid
    elif arry[mid] > mid:
        return binary_search(arry, start, mid - 1)
    elif arry[mid] < mid:
        return binary_search(arry, mid + 1, end)


n = int(input())
arry = list(map(int, input().split()))

print(binary_search(arry, 0 , n - 1))


    



