n, s = map(int, input().split())

nums = []

for _ in range(n):
    nums.append(int(input()))

nums.sort()

case_reached = 0
max_stones = 0
left = 0
right = 0

while right < n and case_reached < 2:
    if abs(nums[left] - nums[right]) > s:
        case_reached += 1
        # max_stones = max(max_stones, right - left)
        max_stones += right - left
        left = right
    right += 1

# max_stones = max(max_stones, right - left)  
print(max_stones)
