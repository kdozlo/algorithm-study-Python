import sys
input = lambda : sys.stdin.readline().rstrip()

a, b = map(int, input().split())

count = 1
while b != a:

    if a > b:
        count = -1
        break

    if b % 10 == 1:
        b //= 10
        count += 1
    else:
        if b % 2 == 0:
            b //= 2
            count += 1
        else:
            count = -1
            break
    
    
print(count)

'''
elif b % 2 == 0:
        b //= 2
        count += 1

#이 경우로 하면 런타임 에러가 뜸
a > b가 아니더라도 2로 나누어 지지 않는다면 끝임, 이 경우도 생각해야함
'''