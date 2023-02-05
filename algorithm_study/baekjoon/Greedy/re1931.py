import sys
input = lambda: sys.stdin.readline().rstrip()

num = int(input())

contime = []
for i in range(num):
    contime.append(list(input()))

contime.sort(key=lambda x:x[0])
contime.sort(key=lambda x:x[1])
print(contime)
f = 0
result = 0
for i in range(num):
    if contime[i][0] >= f:
        result += 1
        f = contime[i][1]

   
print(result)

