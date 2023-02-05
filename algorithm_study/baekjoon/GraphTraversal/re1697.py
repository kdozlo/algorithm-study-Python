import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
Max = 100000


n, k = map(int, input().split())
visited = [0] * (Max + 1)

def bfs():
    q = deque()
    q.append(n)

    while q:
        v = q.popleft()
        if v == k:
            print(visited[v])
            break

        for i in (v-1, v+1, 2*v):
            if 0 <= i <= Max and visited[i] == 0:
                visited[i] = visited[v] + 1
                q.append(i)

bfs()