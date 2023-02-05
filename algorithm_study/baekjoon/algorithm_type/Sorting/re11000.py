import sys
import heapq
input = lambda:sys.stdin.readline().rstrip()

n =int(input())

#a=[list(map(int, input().split())) for _ in range(n)]
a=[]
for _ in range(n):
    s, t = map(int, input().split())
    a.append((s, t))


a.sort()

ah = []
heapq.heappush(ah, a[0][1])

for i in range(1, n):
    if a[i][0] < ah[0]:
        heapq.heappush(ah, a[i][1])
    else:
        heapq.heappop(ah)
        heapq.heappush(ah, a[i][1])

print(len(ah))





