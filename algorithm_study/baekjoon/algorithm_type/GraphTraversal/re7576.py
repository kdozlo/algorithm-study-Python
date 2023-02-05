from collections import deque
import sys
input = lambda:sys.stdin.readline().rstrip()

m,n = map(int, input().split())

graph = []
spoint = [] 

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            spoint.append([i, j]) 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 


def bfs(spoint):
    q=deque()
    for i in spoint:
        q.append(i)

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])
            

   
bfs(spoint)

max = 0
min = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] > max:
            max = graph[i][j]
        if graph[i][j] == 0:
             min = -1
             break
    if i == n-1:
        print(max - 1)
    if min == -1:
        print(min)
        break



