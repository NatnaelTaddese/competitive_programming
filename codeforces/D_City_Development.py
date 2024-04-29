n = int(input())

heights = list(map(int, input().split()))

max_height = 0
max_index = 0

for i in range(n):
    if heights[i] > max_height:
        max_height = heights[i]
        max_index = i

# # trim the lowest

# for i in range(max_index):
#     if heights[i] > heights[i+1]:
#         heights[i] = heights[i+1]

# # trim the highest
# for i in range(max_index + 1, n):
#     if heights[i - 1] < heights[i]:
#         heights[i - 1] = heights[i]

# print(heights)


result = [0] * n

result[max_index] = max_height

current_height = max_height

for i in range(max_index - 1, -1, -1):
    current_height = min(current_height, heights[i])
    result[i] = current_height

current_height = max_height

for i in range(max_index + 1, n):
    current_height = min(current_height, heights[i])
    result[i] = current_height

print(*result)
