import sys
import heapq
input = lambda:sys.stdin.readline().rstrip()
INF = int(1e9)

n, m, x = map(int, input().split()) # n은 학생수와 마을수, x는 출발, m은 간선 수
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e,c))

def dijkstra(start):
    q = []
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    heapq.heappush(q,(0, start))

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))
    
    return distance

d1 = dijkstra(x)
max = 0
for i in range(1, n+1):
    if i == x:
        continue
    d2 = dijkstra(i)
    if max < d1[i] + d2[x]:
        max = d1[i] + d2[x]

print(max)

