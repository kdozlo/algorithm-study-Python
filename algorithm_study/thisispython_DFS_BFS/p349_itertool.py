from itertools import permutations
import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))

symbol = []
symbolNum = list(map(int, input().split()))

for i in range(4):
    if i == 0:
        for j in range(symbolNum[i]):
            symbol.append('+')

    if i == 1:
        for j in range(symbolNum[i]):
            symbol.append('-')

    if i == 2:
        for j in range(symbolNum[i]):
            symbol.append('*')

    if i == 3:
        for j in range(symbolNum[i]):
            symbol.append('/')

min_value = 1e9
max_value = -1e9

symbols = list(permutations(symbol, (n - 1)))

for i in range(len(symbols)):
    now = a[0]
    for j in range(n - 1):
        if symbols[i][j] == '+':
            now = now + a[j+1]
        
        if symbols[i][j] == '-':
            now = now - a[j + 1]
        
        if symbols[i][j] == '*':
            now = now * a[j + 1]

        if symbols[i][j] == '/':
            now = int( now / a[j + 1])
    
    max_value = max(now, max_value)
    min_value = min(now, min_value)
    

print(max_value)
print(min_value)