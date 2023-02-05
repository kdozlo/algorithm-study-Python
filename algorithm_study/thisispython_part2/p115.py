import sys
input = lambda:sys.stdin.readline().rstrip()

x, y = input()
y = int(y)
cnt = 0

nowx = ['a', 'b','c','d','e','f','g','h']

for i in range(len(nowx)):
    if x == nowx[i]:
        x = i + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if nx >= 1 and nx <= 8 and ny >=1 and ny <=8:
        cnt += 1

print(cnt) 
 



