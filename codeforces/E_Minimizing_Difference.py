# n , k = map(int, input().split())

# a = list(map(int,input().split()))

# a.sort()

# left = 0
# right = len(a) - 1

# while(left < right and k > 0):
#     left_diff = a[left + 1] - a[left]
#     right_diff = a[right] - a[right - 1]
#     if left_diff > right_diff and left_diff <= k:
#         a[left] += left_diff
#         k -= left_diff
#     elif left_diff <= right_diff and right_diff <= k:
#         a[right] -= right_diff
#         k -= right_diff



n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

left = 0
right = len(a) - 1

while left < right and k > 0:
    left_diff = a[left + 1] - a[left]
    right_diff = a[right] - a[right - 1]

    if  left_diff <= k:
        a[left] += left_diff
        k -= left_diff
    elif right_diff <= k:
        a[right] -= right_diff
        k -= right_diff
    else:
        break

    while()

# If there are remaining operations, distribute them evenly
remaining_operations = k // (right - left + 1)

# Adjust elements
for i in range(left, right + 1):
    a[i] += remaining_operations

# Calculate minimum possible difference
min_diff = max(a) - min(a)

print(a)
print(min_diff)
# 1 3 5 7