from collections import Counter


for _ in range(int(input())):
    n, c = map(int, input().split())
    planets = list(map(int,input().split()))

    a = Counter(planets)

    total = 0

    for key, value in a.items():
        total += min(value, c)
    
    print(total)