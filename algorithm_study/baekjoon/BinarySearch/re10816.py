import sys
import bisect
import collections
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
my_card = list(map(int, input().split()))

m = int(input())
card = list(map(int, input().split()))

answer = dict()

for num in my_card:
    if num not in answer:
        answer[num] = 1
    else:
        answer[num] += 1

for ans in card:
    if ans in answer:
        print(answer[ans], end=' ')
    else:
        print(0, end=' ')

'''
n = int(input())
my_card = collections.Counter(list(map(int, input().split())))

m = int(input())
card = list(map(int, input().split()))

for i in card:
    if i in my_card:
        print(my_card[i], end=" ")
    else:
        print(0, end=" ")
'''

'''
n = int(input())
my_card = list(map(int, input().split()))

m = int(input())
card = list(map(int, input().split()))
my_card.sort()

for i in card:
    left = bisect.bisect_left(my_card, i)
    right = bisect.bisect_right(my_card, i)
    print(right - left, end=" ")
'''

'''
#런타임 오류...

n = int(input())
my_card = list(map(int, input().split()))

m = int(input())
card = list(map(int, input().split()))
my_card.sort()

def binary_search(ary, target, start, end):
    cnt = 0
    while start <= end:
        mid = (start + end) // 2

        if ary[mid] == target:
            return mid
        elif ary[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return None

for i in card:
    result = binary_search(my_card, i, 0, n-1)
    if result == None:
        print(0, end=" ")
    else:
        cnt = 1
        for j in range(result, -1, -1):
            if my_card[j] != i:
                break
            else:
                cnt = cnt + 1
        
        for j in range(result, n, 1):
            if my_card[j] != i:
                break
            else:
                cnt = cnt + 1

        print(cnt - 2, end=" ")
'''