import sys
input = lambda:sys.stdin.readline().rstrip()


n = int(input())

#cnt는 2부터 시작 1 부터 시작하면 첫 단지에서 방문 여부를 판단 할수 없음 그래서 무한 루프 돔
cnt = 2


graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, -1]

def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    if graph[i][j] == 1:
        graph[i][j] = cnt
        dfs(i-1, j)
        dfs(i, j - 1)
        dfs(i + 1, j)                
        dfs(i, j+1)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            cnt += 1

gnum = []
for i in range(2, cnt):
    sum = 0
    for j in range(n):
        sum += graph[j].count(i)
    gnum.append(sum)

gnum.sort()

cnt -= 2
print(cnt)
for i in gnum:
    print(i)
