import sys
input = lambda:sys.stdin.readline().rstrip()

s = input()
num = 0
ss = []

for i in s:
    if str.isdigit(i):
        num += int(i)
    else:
        ss.append(i)

ss.sort()

if num !=0:
    ss.append(str(num))

print(''.join(ss))
