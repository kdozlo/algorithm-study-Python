import sys
import time
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# 아무래도 뎃셈 연산이 들어가서 조금 느리다. 책의 방식대로 할것.
'''
def dfs(i, j):
    if i <= -1 or i >= n or j <= -1 or j >= m:
        return 0
    if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(i-1, j)
        dfs(i, j - 1)
        dfs(i + 1, j)
        dfs(i, j+1)
        return 1
    return 0


cnt = 0

s = time.time()
for i in range(n):
    for j in range(m):
        cnt += dfs(i, j)
e = time.time()

print(s - e)
print(cnt)
'''

def dfs(i, j):
    if i <= -1 or i >= n or j <= -1 or j >= m:
        return False
    if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(i-1, j)
        dfs(i, j - 1)
        dfs(i + 1, j)
        dfs(i, j+1)
        return True
    return False


cnt = 0

s = time.time()
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1
e = time.time()

print(s - e)
print(cnt)