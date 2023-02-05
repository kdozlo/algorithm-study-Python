import sys
input =lambda:sys.stdin.readline().rstrip()

k, n = map(int, input().split())

rope=[]
for i in range(k):
    rope.append(int(input()))

end = max(rope)
start = 1

while start<=end:
    cnt = 0
    mid = (start + end ) // 2

    for i in rope:
        cnt += i // mid
    
    #필요한 랜선 수보다 작을때 길이를 줄인다.
    if cnt < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)

