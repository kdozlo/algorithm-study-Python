import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

a = [int(input()) for _ in range(n)]

a.sort(reverse=True)

max = a[0]
for i in range(1,n):
    temp = a[i]*(i+1)
    if max < temp:
        max = temp

print(max)
