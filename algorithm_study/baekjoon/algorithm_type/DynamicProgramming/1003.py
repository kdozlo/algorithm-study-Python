import sys
input = lambda:sys.stdin.readline().rstrip()

t = int(input())

n = [int(input()) for _ in range(t)]

dp = [[0]*2 for _ in range(41)] #col = 2, row = 41

dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, max(n) + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

for i in n:
    print(dp[i][0],dp[i][1])
