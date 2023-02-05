import sys

input = lambda: sys.stdin.readline().rstrip()

t = int(input())
num = []
for i in range(t):
    num.append(int(input()))

d = [0] * (max(num) + 1)
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4, max(num) + 1):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]

for i in num:
    print(d[i])
