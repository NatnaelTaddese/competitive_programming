n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

mn = b[0] // a[0]
mx = 0

for i in range(len(a)):
    mn = min(mn, b[i] // a[i])
    mx = max(mx, b[i] + k)

# print(mx, mn)

def can_bake(x):
    k_needed = 0
    for i in range(len(a)):
        required = a[i] * x
        if required > b[i]:
            k_needed += required - b[i]
        if k_needed > k:
            return False
    return True
    


left = mn
right = mx
while left < right:
    
    mid = (left + right + 1) // 2
    if can_bake(mid):
        left = mid
    else:
        right = mid - 1

print(left)