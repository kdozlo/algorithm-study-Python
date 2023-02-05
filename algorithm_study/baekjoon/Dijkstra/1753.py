import sys
import heapq
input = lambda:sys.stdin.readline().rstrip()
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF for _ in range(v+1)]

for _ in range(e):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q,(cost, node[0]))


dijkstra(start)
for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])



        