import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()


def bfs(graph, x, k, visited):
    q = deque([x])
    visited[x] = 1

    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if visited[i] == 0:
                visited[i] = visited[cur] + 1
                q.append(i)




# n = 도시의 개수, m = 도로의 개수, k = 거리 정보, x = 출발 도시 번호
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [0] * (n+1)

bfs(graph, x, k, visited)

for i in range(n+1):
    if visited[i] == k + 1:
        visited[0] = -1
        print(i)

if visited[0] == 0:
    print(-1)




'''
input 예시
4 4 2 1
1 2
1 3
2 3
2 4

output 예시
4
'''

'''
input 예시
4 3 2 1
1 2
1 3
1 4

output 예시
-1
'''

'''
input 예시
4 4 1 1
1 2
1 3
2 3
2 4

output 예시
2
3
'''

