for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    evens = sorted([num for num in a if num % 2 == 0])
    odds = sorted([num for num in a if num % 2 == 1])

    even_idx, odd_idx = 0, 0
    parity = []

    for num in a:
        if num % 2 == 0:
            parity.append(evens[even_idx])
            even_idx += 1
        else:
            parity.append(odds[odd_idx])
            odd_idx += 1

    if parity == sorted(a):
        print("YES")
    else:
        print("NO")
