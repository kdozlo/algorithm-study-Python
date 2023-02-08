from collections import deque
import sys
input = lambda:sys.stdin.readline().rstrip()


#bfs depth 찾는 문제 아니면 dfs로 풀던가.
def bfs(graph, start, end, visited):   
    
    q = deque([start])
    visited[start] = 0

    while q:
        v = q.popleft()

        for i in graph[v]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[v] + 1
                if i == end:
                    return visited[i]

    return visited[end]


n = int(input())
a, b = map(int, input().split())
size = int(input())

relations = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

# y의 부모는 x
for _ in range(size):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)

print(bfs(relations, a, b, visited))

