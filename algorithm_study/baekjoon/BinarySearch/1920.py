import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
m = int(input())
f = list(map(int, input().split())) #찾아야 할 수

a.sort()

def binary_search(ary, target, start, end):
    
    while start <= end:
        mid = (start + end) // 2

        if ary[mid] == target:
            return 1
        elif ary[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return 0

for i in range(m):
    print(binary_search(a, f[i], 0, n-1))