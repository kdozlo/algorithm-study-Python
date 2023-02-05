import sys
import time
input =  lambda: sys.stdin.readline().rstrip()

#교제보다 내 방식이 훨 빠름ㅋㅋ

n, k = map(int, input().split())
count = 0
'''
stime = time.time()
while n != 1:
    if n % k == 0:
        n = n // k
    else:
        n -= 1
    count += 1

print(count)
etime = time.time()
print(etime - stime)

'''

stime = time.time()
while True:
    target = (n // k)*k
    count += (n - target)
    n = target
    if n < k:
        break

    count += 1
    n //= k

count += (n - 1)
print(count)
etime = time.time()

print(etime - stime)
