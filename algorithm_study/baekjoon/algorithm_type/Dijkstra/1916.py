import sys
import heapq
input = lambda:sys.stdin.readline().rstrip()
INF = int(1e9)

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    g[x].append((y,z))

s, e = map(int, input().split())

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in g[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(s)

print(distance[e])
