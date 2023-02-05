import sys
input = lambda:sys.stdin.readline().rstrip()


row, col = map(int, input().split())

x, y, dir = map(int, input().split())

m=[]


for i in range(row):
    m.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

count = 1
turn_time = 0
m[1][1] = 2

while True:
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]

    if m[nx][ny] == 0:
        m[nx][ny] = 2
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        if m[nx][ny] == 2:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)