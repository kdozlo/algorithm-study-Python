import sys
input = lambda:sys.stdin.readline().rstrip()

a = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0]*(max(a)+1)

for i in a:
    count[i] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

        