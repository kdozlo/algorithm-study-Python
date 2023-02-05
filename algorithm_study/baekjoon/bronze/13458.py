import sys
import math
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0

for i in range(N):
    cnt = math.ceil((A[i] - B) / C)
    if (A[i] - B) <= 0:
        continue
    else:
        result += cnt

result += N

print(result)




