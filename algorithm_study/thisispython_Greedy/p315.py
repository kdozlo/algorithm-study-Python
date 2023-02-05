import sys
input = lambda:sys.stdin.readline().rstrip()

'''
# my solve. but O(n) = n^2. so not good, i think...
n, m = map(int, input().split())
k = list(map(int, input().split()))

cnt = 0

for i in range(n):
    for j in range(i+1, n):
        if k[i] == k[j]:
            continue
        else:
            cnt += 1

print(cnt)
'''

n, m = map(int, input().split())
k = list(map(int, input().split()))
weight = [0] * 11

for i in k:
    weight[i] += 1

result = 0
for i in range(1, m+1):
    n -= weight[i]
    result += weight[i] * n

print(result)
