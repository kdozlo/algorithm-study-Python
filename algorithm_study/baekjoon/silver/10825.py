import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

arry = []

for _ in range(n):
    input_data = input().split()
    arry.append((input_data[0], int(input_data[1]), 
                 int(input_data[2]), int(input_data[3])))

arry = sorted(arry, key = lambda s : (-s[1], s[2], -s[3], s[0]))

for s in arry:
    print(s[0])


