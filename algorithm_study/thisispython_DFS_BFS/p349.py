import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))

# + - * /
symbol = list(map(int, input().split()))

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value

    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if symbol[0] > 0:
            symbol[0] -= 1
            dfs(i+1, now + a[i])
            symbol[0] += 1
        
        if symbol[1] > 0:
            symbol[1] -= 1
            dfs(i+1, now - a[i])
            symbol[1] += 1

        if symbol[2] > 0:
            symbol[2] -= 1
            dfs(i+1, now * a[i])
            symbol[2] += 1
        
        if symbol[3] > 0:
            symbol[3] -= 1
            dfs(i+1, int(now / a[i]))
            symbol[3] += 1

dfs(1, a[0])

print(max_value)
print(min_value)