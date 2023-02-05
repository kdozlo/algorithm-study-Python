import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

a = []

for i in range(n):
    input_data = input().split()
    a.append((input_data[0], int(input_data[1])))

a.sort(key= lambda x : x[1])

for i in a:
    print(i[0], end=" ")