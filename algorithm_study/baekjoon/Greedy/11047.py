coin_kind, money = map(int, input().split())
coin_type = []
count = 0

for i in range(coin_kind):
    coin_type.append(int(input()))

coin_type.sort(reverse=True)

for i in coin_type:
    if money >= i:
        count += money // i
        money = money % i

print(count)
