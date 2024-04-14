for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    attacks = 0
    z = 0

    while (sum(a) > 0):
        min_horde = min(a)
        if min_horde <= z:
            for i in range(n):
                if a[i] >= z:
                    a[i] -= z
                    z = 0
                    attacks += 1
                    break
                else:
                    for i in range(n):
                        if a[i] > 0:
                            a[i] -= 1
                            z += 1
                            attacks += 1
                            break
    
    print(attacks)