for _ in range(int(input())):
    n = int(input())
    s = input()
    seen = set()

    curr = 0
    while curr < n:
        if s[curr:n] not in seen:
            seen.add(s[curr:n])
            # curr += 1
            # continue
        # else:
        temp = s[curr] + s[curr+2:n]
        if temp not in seen:
            seen.add(temp)
        
        curr += 1
        
        
        
    print(len(seen))

'''
ababa
baba
aba
ba
a

'''