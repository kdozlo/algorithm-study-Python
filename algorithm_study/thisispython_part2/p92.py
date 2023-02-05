import sys
input = lambda:sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort(reverse=True)

sum = (num_list[0] * 3 + num_list[1]) * (M // (K+1))
sum += num_list[0] * (M % (K+1))

'''
sum = 0
count = 0
for i in range(M):
    count += 1
    if count > K:
        count = 0
        sum += num_list[1]
    else:
        sum += num_list[0]
'''

print(sum)