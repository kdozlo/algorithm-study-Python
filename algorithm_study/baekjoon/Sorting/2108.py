import sys
from collections import Counter
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

a = [int(input()) for _ in range(n)]

a.sort()

#1
if round(sum(a)/n) == -0:
    print(0)
else:
    print(round(sum(a)/n))

#2
print(a[n//2])

#3

if n == 1:
    print(a[0])
else:
    fre_a = Counter(a).most_common(2)
    if fre_a[0][1] == fre_a[1][1]:
        print(fre_a[1][0])
    else:
        print(fre_a[0][0])

#4
print(a[-1] - a[0])