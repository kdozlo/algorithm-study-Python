import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
plist=[]
plist = list(map(int, input().split()))

plist.sort()

now = 0
cnt = 0
while True:
    now += plist[now]
   
    if now >= n:
        break

    cnt += 1

print(cnt)
