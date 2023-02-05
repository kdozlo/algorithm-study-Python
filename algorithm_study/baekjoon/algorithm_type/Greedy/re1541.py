import sys
input = lambda: sys.stdin.readline().rstrip()


data = input().split('-')

ad_data = []
result = 0

for i in range(len(data)):
    k=0
    s=data[i].split('+')
    for j in s:
        k += int(j)
    ad_data.append(k)

result = ad_data[0]

for i in range(1, len(ad_data)):
    result -= ad_data[i]
    
print(result)



