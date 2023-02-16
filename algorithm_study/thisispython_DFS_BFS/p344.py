import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()


#n은 n행 n열, k는 바이러스 종류
n, k = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

#s는 초
s, x, y = map(int, input().split())

data = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], i, j, 0))

data.sort()

q = deque(data)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    curv, curx, cury, curs = q.popleft()

    if curs == s:
        break

    for i in range(4):
        nx = curx + dx[i]
        ny = cury + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < n :
            if graph[nx][ny] == 0:
                graph[nx][ny] = curv
                q.append((curv, nx, ny, curs + 1))


print(graph[x - 1][y - 1])


                
       
       


