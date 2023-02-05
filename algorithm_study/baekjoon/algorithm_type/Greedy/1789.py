import sys
input = lambda:sys.stdin.readline().rstrip()

s = int(input())

i = 1
cnt = 1
while s:
    if s - i < i + 1:
        break
    s -= i
    i += 1
    cnt += 1
    

print(cnt)