n = int(input())

total = 0

for i in range(2,n + 1):
    prime_factors = []
    for j in range(2,i):
        if i % j == 0:
            prime_factors.append(j)
    if len(prime_factors) == 2:
        print(prime_factors)
        total += 1

print(total)

