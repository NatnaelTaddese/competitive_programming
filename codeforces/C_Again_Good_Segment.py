from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = 0
result = 0
mode = 0
mode_count = 0
num_count = defaultdict(int)

while right < n:
    num_count[nums[right]] += 1

    if num_count[nums[right]] > mode_count:
        mode = nums[right]
        mode_count = num_count[nums[right]]

    while right - left + 1 > mode_count:
        num_count[nums[left]] -= 1
        if num_count[nums[left]] == 0:
            del num_count[nums[left]]
        left += 1

    if mode_count >= k:
        result += 1

    right += 1

print(result)
