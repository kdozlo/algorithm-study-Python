import sys
input = lambda:sys.stdin.readline().rstrip()

#계수 정렬 방법, 집합 자료형 방법도 익히자!

def binary_search(ary, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if ary[mid] == target:
            return 1
        elif ary[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return 0

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
f = list(map(int, input().split()))

for i in range(m):
    if binary_search(a, f[i], 0, n - 1) == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
