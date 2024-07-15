n, t = map(int,input().split())

a = list(map(int,input().split()))

curr = 1

while curr < t:
    curr += a[curr - 1]
    if curr == t:
        print("YES")
        exit()
    
print("NO")