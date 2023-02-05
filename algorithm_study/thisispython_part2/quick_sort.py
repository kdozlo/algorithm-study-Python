import sys
input = lambda:sys.stdin.readline().rstrip()


a = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and a[left] <= a[pivot]:
            left += 1

        while right > start and a[right] >= a[pivot]:
            right -= 1

        if left > right:
            a[right], a[pivot] = a[pivot], a[right]
        else:
            a[left], a[right] = a[right], a[left]

    quick_sort(a, start, right-1)
    quick_sort(a, right+1, end)


def quick_sort_py(a):
    if len(a) <= 1:
        return a
    
    pivot = a[0]
    tail = a[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + pivot + quick_sort(right_side)