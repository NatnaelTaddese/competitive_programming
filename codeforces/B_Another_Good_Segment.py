n, s = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
result = 0
distinct_count = 0
num_count = {}

for right in range(n):
    num_count[nums[right]] = num_count.get(nums[right], 0) + 1

    if num_count[nums[right]] == 1:
        distinct_count += 1

    while distinct_count > s:
        num_count[nums[left]] -= 1
        if num_count[nums[left]] == 0:
            distinct_count -= 1
            del num_count[nums[left]]
        left += 1

    result += right - left + 1

print(result)
