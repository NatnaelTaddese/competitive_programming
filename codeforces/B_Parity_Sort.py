for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    # compare= sorted(nums)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if (nums[j] % 2 == nums[min_idx] % 2) and nums[j] < nums[min_idx]:
                min_idx = j
        
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
        # if nums[i] != compare[i]:
        #     print("NO")
        #     break
    
    # if nums == sorted(nums):
    #     print("YES")
    # else:
    #     print("NO")
    # if nums == compare:
    #     print("YES")
    # 1234
    passed = True
    for i in range(1, n):
        if nums[i] < nums[i -1]:
            passed = False
            print("NO")
            break
    if passed == True:
        print("YES")