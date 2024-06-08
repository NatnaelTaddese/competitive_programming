
def backtrack(arr, target):

    
    if sum(arr) == target:
        return True
    
    if max(arr) == min(arr):
        return False


    
    mid = (max(arr) + min(arr)) // 2

    left = []
    right = []
    
    for val in arr:
        if val <= mid:
            left.append(val)
        else:
            right.append(val)



    if backtrack(left, target):
        return True
    
    if backtrack(right, target):
        return True

    return False


for _ in range(int(input())):
    n, q = map(int,input().split())

    a = list(map(int,input().split()))

    for _ in range(q):
        s = int(input())
        res = backtrack(a,s)
        if res:
            print("Yes")
        else:
            print("No")