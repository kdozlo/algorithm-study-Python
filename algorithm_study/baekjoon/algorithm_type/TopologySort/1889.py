import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
check = [0] * (n+1)

for i in range(1, n+1):
    a, b = map(int, input().split())
    graph[i].append(a)
    graph[i].append(b)
    indegree[a] += 1
    indegree[b] += 1



def topology_sort():
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0 or indegree[i] == 1:
            q.append(i)
            check[i] = 1
            
    
    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            if check[i] == 0:    
                if indegree[i] == 0 or indegree[i] == 1:
                    q.append(i)
                    check[i] = 1

topology_sort()
cnt = 0

for i in range(1, n+1):
    if indegree[i] == 2:
        cnt += 1

if cnt <= 2:
    print(0)
else:
    print(cnt)
    for i in range(1, n+1):
        if indegree[i] == 2:
            print(i, end=' ')