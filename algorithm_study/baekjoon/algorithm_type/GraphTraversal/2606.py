import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(graph, i, visited)

graph = [[] for _ in range(n+1)]
for i in range(m):
    e, s = map(int, input().split())
    graph[e].append(s)
    graph[s]. append(e)

for i in range(1, n+1):
    graph[i].sort()

visited = [0] * (n+1)
dfs(graph, 1, visited)
print(sum(visited)-1)

