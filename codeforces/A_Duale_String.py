for _ in range(int(input())):
    s = input()
    n = len(s)

    if n % 2 != 0:
        print("NO")
        continue
    else:
        mid = n//2
        if s[:mid] == s[mid:]:
            print("YES")
        else:
            print("NO")

#two pointers