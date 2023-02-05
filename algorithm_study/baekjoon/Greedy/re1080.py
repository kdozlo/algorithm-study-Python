import sys
input =  lambda : sys.stdin.readline().rstrip()

def check(mat, i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            mat[x][y] = 1 - mat[x][y]
    
    return mat


n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    a.append(list(map(int, input())))

for i in range(n):
    b.append(list(map(int, input())))

cnt = 0

for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            cnt += 1
            a = check(a, i, j)

if a == b:
    print(cnt)
else:
    print(-1)
    
