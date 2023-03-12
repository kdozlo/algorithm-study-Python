from itertools import combinations
import sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())

map = []
t = []
spaces = []


for i in range(N):
    map.append(list(input().split()))
    for j in range(N):
        if map[i][j] == 'T':
            t.append((i, j))
        
        if map[i][j] == 'X':
            spaces.append((i, j))

def watch(x, y, direction):
    #left
    if direction == 0:
        while y >= 0:
            if map[x][y] == 'S':
                return True
            if map[x][y] == 'O':
                return False
            y -= 1
    
    #right
    if direction == 1:
        while y < N:
            if map[x][y] == 'S':
                return True
            if map[x][y] == 'O':
                return False
            y += 1

    #up
    if direction == 2:
        while x >= 0:
            if map[x][y] == 'S':
                return True
            if map[x][y] == 'O':
                return False
            x -= 1

        #down
    if direction == 3:
        while x < N:
            if map[x][y] == 'S':
                return True
            if map[x][y] == 'O':
                return False
            x += 1

    return False

def process():
    for x, y in t:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False

for data in combinations(spaces, 3):
    for x, y in data:
        map[x][y] = 'O'
    
    if not process():
        find = True
        break
    for x,y in data:
        map[x][y] = 'X'


if find:
    print('YES')
else:
    print('NO')    





