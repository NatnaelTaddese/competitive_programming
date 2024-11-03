n = int(input())
arr = list(map(int, input().split()))

mx_consecutive = 1
curr = 1

for i in range( n - 1):
    if arr[i] < arr[i + 1]:
        curr += 1
    else:
        mx_consecutive = max(mx_consecutive, curr)
        curr = 1
    
print(max(mx_consecutive, curr))
