n , t = map(int, input().split())
a = list(map(int, input().split()))

total = sum(a)

# left = 0
# right = n - 1

# # print(total, a)

# while(left <= right):
#     if total <= t:
#         print((right - left) + 1)
#         break
#     if a[left] > a[right]:
#         total -= a[left]
#         left += 1
#     else:
#         total -= a[right]
#         right -= 1

left = 0
right = 0

total = 0
max_book = 0

while right < n:
    if total + a[right] <= t:
        total += a[right]
        right += 1
        max_book = max(max_book, right - left)
    else:
        total -= a[left]
        left += 1

print(max_book)
