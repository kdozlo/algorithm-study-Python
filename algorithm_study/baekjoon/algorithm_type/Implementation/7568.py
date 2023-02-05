import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
g = []

for i in range(n):
    g.append(list(map(int, input().split())))
    g[i].append(i)

rank = 1
for i in range(n):
    for j in range(n):
        if g[i][0] < g[j][0] and g[i][1] < g[j][1]:
            rank += 1
        else:
            continue
    
    print(rank, end=" ")
    rank = 1
  

    
