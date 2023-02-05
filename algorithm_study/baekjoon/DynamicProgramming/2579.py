import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
step=[]
for i in range(n):
    step.append(int(input()))

dp = [0] * n 

dp[0] = step[0]

if n >= 2:
    dp[1] = step[0] + step[1]
    
if n >= 3:
    dp[2] = max(step[0] + step[2], step[1] + step[2])

    for i in range(3, n):
        dp[i] = max(dp[i - 2], dp[i - 3] + step[i - 1])
        dp[i] += step[i]


print(dp[n - 1])
