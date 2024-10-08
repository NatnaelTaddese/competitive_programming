
coins = []

def is_pal(num):
    return num == int(str(num)[::-1])

LIMIT = (4 * 10 ** 4) + 10
M = (10 ** 9) + 7

for i in range(1, LIMIT):
    if is_pal(i):
        coins.append(i)

memo = [0 for _ in range(LIMIT + 1)]
memo[0] = 1


for coin in coins:
    for i in range(coin, LIMIT + 1):
        memo[i] += memo[i - coin] % M
        memo[i] %= M

for _ in range(int(input())):
    n = int(input())

    print(memo[n])