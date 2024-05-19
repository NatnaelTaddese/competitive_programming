for _ in range(int(input())):
    n = int(input())
    weight = list(map(int, input().split()))
    # alex_prefix_sum = [0] * (n + 1)
    # for i in range(1, n + 1):
    #     alex_prefix_sum[i] = alex_prefix_sum[i - 1] + weight[i - 1]
    
    # #debug
    # print(alex_prefix_sum)
    # bob_prefix_sum = [0] * (n + 1)

    # for i in range(n - 1, -1,-1):
    #     bob_prefix_sum[i] = bob_prefix_sum[i+1] + weight[i]
    
    # # bob_prefix_sum = reversed(bob_prefix_sum)
    # print(bob_prefix_sum)

    # i = 1
    # j = n - 2

    # ans = 0 
    # while (i < j):
    #     if 
    
    # trying balancing from both sides

    left = 0
    right = n - 1

    alex, bob = 0, 0

    ans = 0

    while left <= right:
        if alex < bob:
            alex += weight[left]
            left += 1
        else:
            bob += weight[right]
            right -= 1
        
        if alex == bob:
            ans = left + (n - right - 1)
        
    print(ans)
    