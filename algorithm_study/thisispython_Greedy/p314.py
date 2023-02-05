import sys
input = lambda:sys.stdin.readline().rstrip()

import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
coin = list(map(int, input().split()))
coin.sort()

target = 1
for x in coin:
    if target < x:
        break
    target += x

print(target)

