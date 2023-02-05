import sys
input = lambda : sys.stdin.readline().rstrip()

tnum = int(input())

for i in range(tnum):
    pnum = int(input())
    rank = []

    for j in range(pnum):
        a, b = list(map(int, input().split()))
        rank.append([a, b])
    
    rank.sort()
    min = rank[0][1]
    count = 1

    for j in range(pnum):
        if rank[j][1] < min:
            min = rank[j][1]
            count += 1

    print(count)

#   del rank => 메모리도 안줄고 시간만 잡아 먹음 없는게 좋은듯....
