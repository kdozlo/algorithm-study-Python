import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)

n, k = map(int, input().split())
graph = [[] for _ in range(200001)]
distance = [INF] * 200001

graph[0].append((1, 1))
graph[0].append((0, 0))
for i in range(1, 100001):
    graph[i].append((i-1, 1))
    graph[i].append((i+1, 1))
    graph[i].append((i*2, 0))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist < distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(n)

print(distance[k])

#bfs로도 풀어보기