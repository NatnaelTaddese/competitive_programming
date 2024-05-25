def find_water_area(heights, wall):
    area = 0

    for height in heights:
        if height < wall:
            area += wall - height
    
    return area
    # return sum(max(0,wall - height) for height in heights)

def find_water_area_list(heights, wall):
    area = []

    for height in heights:
        if height < wall:
            area.append(wall - height)
        else:
            area.append(0)

    
    return area


for _ in range(int(input())):
    n , x = map(int, input().split())
    heights = list(map(int,input().split()))
    max_height = max(heights)
    min_height = min(heights)

    # do binary search on the wall to find the optimal height
    left = 0
    right = x + max_height

    while left < right:
        # mid = (left + right + 1) // 2
        mid = left + (right - left + 1) // 2
        if find_water_area(heights, mid) <= x:
            left = mid
        else:
            right = mid - 1
    
    # print(find_water_area(heights, left-1), find_water_area_list(heights, left-1))
    # while find_water_area(heights,left) > x:
    #     left -= 1

    print(left)