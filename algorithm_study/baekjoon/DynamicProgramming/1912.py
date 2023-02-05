import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

ary = list(map(int, input().split()))

dp = [-1000] * n

dp[0] = ary[0]
for i in range(1, n):
    dp[i] = (max(dp[i - 1]+ary[i], ary[i]))

print(max(dp))