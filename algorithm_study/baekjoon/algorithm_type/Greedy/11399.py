import sys
input = lambda:sys.stdin.readline().rstrip()

pnum = int(input())

totaltime = 0

worktime = list(map(int, input().split()))

worktime.sort(reverse=True)

for i in range(pnum):
    totaltime += worktime[i]*(i+1) 
# (pnum-i)보다 (i+1)가 빠르다. 즉 덧셈이 더 빠름

print(totaltime)
