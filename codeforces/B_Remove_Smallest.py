for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    found = False

    for i in range(len(a) - 1):
        if abs(a[i] - a[i+1]) > 1:
            print("NO")
            found = True
            break
    
    if not found:
        print("YES") 