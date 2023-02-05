import sys
input = lambda:sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)


 

t = int(input())
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, -1]

def dfs(graph, i, j, m, n):
    if i < 0 or i >= m or j < 0 or j >= n:
        return False
    if graph[i][j] == 1:
        graph[i][j] = 0

        dfs(graph, i-1, j, m, n)
        dfs(graph, i, j - 1, m, n)
        dfs(graph, i + 1, j, m, n)                
        dfs(graph, i, j+1, m, n)
        return True

    return False

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(m):
        for j in range(n):
            if dfs(graph, i, j, m, n):
                cnt += 1
    
    print(cnt)
    cnt = 0
    

""" 
import sys
input = sys.stdin.readline

def bfs(x, y):
    visit = [[x, y]]
    while visit:
        p = visit.pop(0)
        x, y = p[0], p[1]
        if 0 <= x < m and 0 <= y+1 < n and L[y+1][x] == 1:
            L[y+1][x] = 0
            visit.append([x, y+1])
        if 0 <= x+1 < m and 0 <= y < n and L[y][x+1] == 1:
            L[y][x+1] = 0
            visit.append([x+1, y])
        if 0 <= x < m and 0 <= y-1 < n and L[y-1][x] == 1:
            L[y-1][x] = 0
            visit.append([x, y-1])
        if 0 <= x-1 < m and 0 <= y < n and L[y][x-1] == 1:
            L[y][x-1] = 0
            visit.append([x-1, y]) 

T = int(input())    
for _ in range(T):
    m, n, k = map(int, input().split())
    L = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        L[b][a] = 1
    cnt = 0
    
    for x in range(m):
        for y in range(n):
            if L[y][x] == 1:
                bfs(x, y)
                cnt += 1
    print(cnt)
 """




