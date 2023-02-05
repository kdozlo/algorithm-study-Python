import sys
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = list(map(int, input().split()))

start = 0
end = max(a)

while start <= end:
    mid = (start + end ) // 2

    sum = 0
    for i in a:
        if i > mid:
            sum = sum + i - mid
    '''
    if sum == m:
        print(mid)
        sys.exit()
    '''
    #떡 양이 부족한 경우 기준을 낮춘다
    if sum < m:
        end = mid - 1
    else:
        start = mid + 1


print(end)