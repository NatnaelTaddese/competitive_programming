
#  Sieve of Eratosthenes

import math


# LIMIT = 10**5 + 10
LIMIT = 10**6

is_prime = [True for _ in range(LIMIT + 1)]
is_prime[0] = is_prime[1] = False

for i in range(2, int(math.sqrt(LIMIT)) + 1):
    if is_prime[i]:
        for j in range(i * i, LIMIT + 1, i):
            is_prime[j] = False
"""
1 .... some number .... n = 3Factors
only one number
it has to be the square of the number

"""

# solutions = set()
# for i in range(2, LIMIT + 1):
#     if is_prime[i]:
#         solutions.add(i**i)
t_primes = {i * i for i in range(2, LIMIT + 1) if is_prime[i]}

# print(solutions)

# solutions = []
n = int(input())

test_cases = list(map(int, input().split()))

# for test_case in test_cases:
#     if test_case in solutions:
#         print('YES')
#     else:
#         print('NO')

output = []
for x in test_cases:
    if x in t_primes:
        output.append("YES")
    else:
        output.append("NO")

print("\n".join(output))

