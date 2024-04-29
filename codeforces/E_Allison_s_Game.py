n = int(input())

height = list(map(int, input().split()))


# max_area = 0
max_width = 0


# its square not rectangle ayiii
left = 0

while left < n:

    right = left
    width = 0
    
    while right < n:
        if height[left] == height[right]:
            width += 1
            right += 1
            if height[left] == width:
                max_width = max(max_width, width)
                # print(height[left:right])
                # print(height[left], width)

                break
        else:
            break
    # area = width * height[left]
    # # print(area)

    # if area > max_area:
    #     max_width = width
    #     max_area = area
    
    left = right


# trying sliding window instead.....

# for i in range(n):
#     width = 1
#     # Traverse leftwards from the current bar
#     for j in range(i - 1, -1, -1):  
#         if height[j] >= height[i]:
#             width += 1
#         else:
#             break
#     # Traverse rightwards from the current bar
#     for j in range(i + 1, n):  
#         if height[j] >= height[i]:
#             width += 1
#         else:
#             break
#     max_width = max(max_width, min(width, height[i]))


print(max_width)