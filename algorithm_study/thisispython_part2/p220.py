import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
path = list(map(int, input().split()))

d = [0] * 1001

d[0] = path[0]
d[1] = max(d[0], path[1])
for i in range(2, n):
    d[i] = max(d[i-2] + path[i], d[i - 1])

print(d[n-1])