import sys
input = lambda:sys.stdin.readline().rstrip()

n = input()
num1 = 0
num2 = 0

for i in range(len(n) // 2):
    num1 += int(n[i])

for i in range(len(n) // 2, len(n)):
    num2 += int(n[i])

if num1 == num2:
    print('LUCKY')
else:
    print('READY')
    