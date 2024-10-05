
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    # if len(set(a)) == 1:
    #     print("NO")
    #     continue

    prefix_sum = 0
    balanced = True
    # running = 0
    # for i in range(n):
    #     if a[i] != running:
    #         running += a[i]
    #     else:
    #         print("YES")
    #         print(*a)
    #         break
    # else:
    #     mx = max(a)
    #     print("max: ", mx)
    #     mn = a[0]
    #     a[a.index(mx)] = mn
    #     a[0] = mx
    #     print("YES")
    #     print(*a)
    
    
    # print("YES")
    # a[0], a[-1] = a[-1], a[0]
    # print(*a)


    for i in range(n):
        if a[i] == prefix_sum:
            balanced = False
            break
        prefix_sum += a[i]

    if balanced:
        print("YES")
        print(*a)
    else:
        a.sort(reverse=True)
        prefix_sum = 0
        balanced = True

        for i in range(1, n):
            if a[i] == prefix_sum:
                balanced = False
                break
            prefix_sum += a[i]

        if balanced:
            print("YES")
            print(*a)
        else:
            print("NO")