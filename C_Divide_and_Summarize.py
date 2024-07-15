
seen= set()

def backtrack(arr):

    
    
    mn = min(arr)
    mx = max(arr)

    seen.add(sum(arr))
    
    if mx == mn:
        return False


    
    mid = (mx + mn) // 2

    left = []
    right = []
    
    for val in arr:
        if val <= mid:
            left.append(val)
        else:
            right.append(val)



    backtrack(left)
    
    backtrack(right)



for _ in range(int(input())):
    n, q = map(int,input().split())

    a = list(map(int,input().split()))

    seen.clear()

    backtrack(a)

    for _ in range(q):
        s = int(input())
        if s in seen:
            print("Yes")
        else:
            print("No")