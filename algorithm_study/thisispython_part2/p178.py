import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

a = []

for i in range(n):
    a.append(int(input()))

a.sort(reverse=True)

for i in a:
    print(i, end=" ")