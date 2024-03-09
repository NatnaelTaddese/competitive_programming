for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    swaps = 0

    if a == b:
        print(swaps)
        continue

    for i in range(n - 1, 0,-1):
        if b[i] == a[i]:
            continue
        cursor = i - 1
        while(cursor > 0):
            if a[cursor] == b[i]:
                a[cursor], a[i] = a[i], a[cursor]
                swaps += 1
                break
            else:
                cursor -= 1
        
    print(swaps + 1)
