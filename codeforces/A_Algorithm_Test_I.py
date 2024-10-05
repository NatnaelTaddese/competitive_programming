from collections import Counter
from math import factorial


m = int(input())
a = list(map(int, input().split()))
a = Counter(a)

ballons = list(a.keys())

ways = factorial(len(ballons))

print(ways)