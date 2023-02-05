import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

a = list(map(int, input().split()))

d = [0] * (1000)

for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            d[i] = max(d[i], d[j] + 1)

print(max(d) + 1)