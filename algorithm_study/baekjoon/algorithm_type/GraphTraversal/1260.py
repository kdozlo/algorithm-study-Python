from collections import deque
import sys
input = lambda:sys.stdin.readline().rstrip()

def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    q = deque()
    visited[v] = 1
    q.append(v)
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(n+1):
    graph[i].sort()

visited = [0] * (n+1)
dfs(graph, v, visited)
print()
visited = [0] * (n+1)
bfs(graph, v, visited)
