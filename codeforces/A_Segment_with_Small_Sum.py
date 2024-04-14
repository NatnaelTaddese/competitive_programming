n, s = map(int, input().split())

nums = list(map(int, input().split()))

left = 0
# right = n - 1

# sum = sum(nums)
# solved = False



right = 0
current_sum = 0
max_length = 0

while right < n:
    current_sum += nums[right]
    # if current_sum > s:
    while current_sum > s:
        current_sum -= nums[left]
        left += 1
    max_length = max(max_length, right - left + 1)
    right += 1

print(max_length)


