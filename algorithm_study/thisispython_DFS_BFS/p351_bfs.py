#https://fre2-dom.tistory.com/436 블로그 참조
import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

map = []
teachers = []
spaces = []

for i in range(n):
    map.append(list(input().split()))
    for j in range(n):
        if map[i][j] == 'T':
            teachers.append((i, j))

        if map[i][j] == 'X':
            spaces.append((i, j))


def backTracking(cnt):
    global flag

    if cnt == 3:
        if bfs():
            flag = True
            return
    else:
        for x in range(n):
            for y in range(n):
                if map[x][y] == 'X':
                    map[x][y] = 'O'
                    backTracking(cnt + 1)
                    map[x][y] = 'X'

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for t in teachers:
        for k in range(4):
            nx, ny = t

            while 0 <= nx < n and 0 <= ny < n:
                if map[nx][ny] == 'O':
                    break
                
                if map[nx][ny] == 'S':
                    return False
            
                nx += dx[k]
                ny += dy[k]
    
    return True

flag = False
backTracking(0)

if flag:
    print("YES")
else:
    print("NO")


