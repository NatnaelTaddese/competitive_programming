# for _ in range(int(input())):
#     n = int(input())
#     nums = list(map(int, input().split()))
    # result = 0

    # left = 0
    # right = left + 1

    # for i in range(n):
    #     valid = 0
    #     index = 0
    #     if nums[i] >= i:
    #         index += 1
    #         valid += 1
    #         print("[",nums[i], end="] ")


    #         while(right < n):
    #             if nums[right] >= index:
    #                 valid+=1
    #                 print(nums[right], end=" ")

    #             else:
    #                 break
    #             right += 1
    #             index += 1
        
    #     result += valid
        
    #     right = i+2
    
    # print(result)

    # index = 0

    # while(right < n):
    #     if  nums[left] >= index:
    #         result += 1
    #         index += 1
    #         if nums[right] >= index:
    #             result += 1
    #             index += 1
    #     else:
    #         index = 0
    #         continue
        
    # result = 0

    # left = 0
    # right = 0


    # for i in range(n):
    #     index = 1
    #     if nums[i] >= index:
    #         result += 1
    #         index += 1
    #         # print(i, end = " ")
    #         for j in range(i + 1, n):
    #             if nums[j] >= index:
    #                 # print("[", j  ,"] ",end="")
    #                 result += 1
    #                 index += 1
    #             else:
    #                 break
    #     else:
    #         continue
    # print(result)

    # result = 0
    
    # left = 0
    # right = 0
    # index = 1

    # while left < n:
    #     while right < n and nums[right] >= index:
    #         right += 1
    #         index += 1
        
    #     result += right - left
        
    #     left += 1
        
    #     # if right < n and nums[right] < index:
    #     #     index = 1
    #     #     right = left

    #     while right < n and nums[right] < index:
    #         index = 1
    #         right -= 1
            

    #         # 1 2 3 4 5 6 ... n
    #         # 1st : n elements 
    #         # left += 1
    
    # print(result)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    # i, j, res = 0, 0, 0
    # while j < n:
    #     if a[j] >= (j - i + 1):
    #         res += j - i + 1
    #         j += 1
    #     else:
    #         i += 1
    # print(res)
    l = 0
    r = 0
    count = 0
    while r < n:
        if a[r] >= (r - l + 1):
            count += r - l + 1
            r += 1
        else:
            l += 1
    
    print(count)