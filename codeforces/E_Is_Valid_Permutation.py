for _ in range(int(input())):
    seen = set()
    n = int(input())
    pref = list(map(int, input().split()))

    seen.add(pref[0])

    for i in range(1, len(pref)):
        seen.add((pref[i] - pref[i-1]))
    
    if len(seen) == len(pref) or len(seen) - 1 == len(pref):
        print("YES")
    else:
        print("NO")
    
    # 13 ,21, 36 42
    # 13, 8, 15, 6
        
    # 5 44 46 50
    # 5 39 2 4
    # 3 7 10
    # 3 5 3
