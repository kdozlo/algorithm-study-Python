import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

route = list(map(str, input().split()))

x = 1
y = 1

for i in range(len(route)):
    if route[i] == 'L':
        if x > 1:
            x -= 1
    elif route[i] == 'R':
        if x < n:
            x += 1
    elif route[i] == 'U':
        if y > 1:
            y -= 1
    elif route[i] == 'D':
        if y < n:
            y += 1

print(x,y)