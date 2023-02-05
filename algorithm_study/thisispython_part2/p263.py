import sys
import heapq
input = lambda:sys.stdin.readline().rstrip()
INF = int(1e9)

#c에서 시작, 최대한 많이 퍼지게, 걸리는 시간
n, m, c = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)
print(distance)
cnt = 0
cost = 0
for i in distance:
    if i != INF:
        cnt += 1
        if i > cost:
            cost = i

print(cnt-1, cost)

#플로이드 워셜 알고리즘으로 풀어본건데 이게 맞는지는 알수 없음....
'''
#c에서 시작, 최대한 많이 퍼지게, 걸리는 시간
n, m, c = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x][y] = z

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

cnt = 0
for i in range(1, n+1):
    if graph[c][i] != INF and i != c:
        cnt += 1

print(cnt, max(graph[c]))
'''