import sys
input = lambda:sys.stdin.readline().rstrip()

def dfs(graph, start, visited):
    for i in graph[start]:
        if visited[i] == 0:
            visited[i] = visited[start] + 1
            dfs(graph, i,  visited)


n = int(input())
a, b = map(int, input().split())
num = int(input())

relations = [[] for _ in range(n + 1)]

for _ in range(num):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)

visited = [0] * (n + 1)

dfs(relations, a, visited)

print(visited[b] if visited[b] > 0 else -1)
