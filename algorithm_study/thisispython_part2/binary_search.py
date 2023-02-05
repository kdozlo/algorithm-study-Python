import sys
input = lambda:sys.stdin.readlin().rstrip()

def binary_search_r(arry, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if arry[mid] == target:
        return mid
    elif arry[mid] > target:
        return binary_search_r(arry, target, start, mid-1)
    else:
        return binary_search_r(arry, target, mid+1, end)

def binary_search(arry, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arry[mid] == target:
            return mid
        elif arry[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None    
    