import sys
import heapq
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

cards = []

for _ in range(n):
    heapq.heappush(cards, int(input()))

if n == 1:
    print(0)
elif n > 1:
    compare = 0
    result = 0
    cnt = 0

    while cnt < n - 1:
        cnt += 1
        compare = heapq.heappop(cards) + heapq.heappop(cards)
        heapq.heappush(cards, compare)
        result += compare
    
    print(result)


   
 

   

