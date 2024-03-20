for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    start = 0
    result = 0

    while start < len(nums):
        temp = start
        sign = nums[temp] > 0
        curr = nums[temp]

        while temp < n and ((nums[temp] > 0) == sign) :
            curr = max(curr, nums[temp])
            temp += 1

        start = temp
        result += curr

    print(result)