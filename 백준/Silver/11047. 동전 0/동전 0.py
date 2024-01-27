n, k = input().split()
# print(n, k)
coin = []
min = 0
money = int(k)


for _ in range(int(n)):
    coin.append(int(input()))

coin.sort(reverse=True)
# print(coin)

for i in coin:
    if money // i >= 1:
        min += money//i
        # print(min)
        money = money % i
        # print(money)
       
print(min)