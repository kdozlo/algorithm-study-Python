import sys
input = lambda:sys.stdin.readline().rstrip()

city_num = int(input())
road_len = list(map(int, input().split()))
oil_expense = list(map(int, input().split()))

mincost = oil_expense[0]*road_len[0]

min = oil_expense[0]
for i in range(0, city_num - 2):
    if min > oil_expense[i+1]:
        min = oil_expense[i+1]
    mincost += min * road_len[i+1]

print(mincost)

'''
# 58점, runtime over 인듯...
sort_oil_expense = sorted(oil_expense)

index = 0 #정렬된 오일값 리스트의 index
Rindex = 0 #정렬된 오일값 리스트의 원래 index
PRindex = city_num - 1 
mincost = 0
while index < city_num:
    min = sort_oil_expense[index]

    #원래 오일값 리스트의 index 찾기
    for i in range(city_num):
        if min == oil_expense[i]:
            Rindex = i
            break
    
    if Rindex > PRindex:
        index += 1
        continue

    if Rindex == (city_num - 1):
        index += 1
        continue
    
    for i in range(Rindex, PRindex):
        mincost += sort_oil_expense[index] * road_len[i]
    
    if Rindex == 0:
        break
    else:
        PRindex = Rindex
        index += 1


print(mincost)
'''

