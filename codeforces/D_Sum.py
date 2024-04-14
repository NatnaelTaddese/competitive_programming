for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    nums.sort()

    i = 0
    j = len(nums) - 1

    op_left = k

    for _ in range(k):
        # two_smallest = nums[i] + nums[i+1]
        # largest = nums[j]

        # if two_smallest < largest:
        #     i += 2
        # else:
        #     j -= 1
        smalls = 0

        for c in range(i, i + op_left + 2):
            smalls += nums[c]

        larges = 0

        for c in range(j, j - op_left, - 1):
            larges += nums[c]
        
        if smalls < larges:
            i += 2
            op_left -= 1
        else:
            j -= 1
            op_left -= 1
        
        # print(smalls, larges)

    result = 0
    
    for i in range(i,j+1):
        result += nums[i]

    print(result)

# 10, 11, 12, 13, 15, 22
    
# remove = 37 to get 46
    # 22 + 15
    # 10 + 12 + 15

    