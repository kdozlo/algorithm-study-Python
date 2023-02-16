import sys
input = lambda:sys.stdin.readline().rstrip()

n, c = map(int, input().split())
arry = []

for _ in range(n):
    arry.append(int(input()))

arry.sort()

start = 1
end = arry[-1] - arry[0]
result = 0

while(start <= end):
    mid = (start + end) // 2
    value = arry[0]
    count = 1

    for i in range(1, n):
        if arry[i] >= value + mid:
            value = arry[i]
            count += 1
    
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1


print(result)





