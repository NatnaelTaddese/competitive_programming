from math import floor


# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))

#     dp = [0 for _ in range(n)]
#     # dp = [[0] * 15 for _ in range(n)]

#     # for x in range(15):
#     #     dp[n-1][x] = max(a[n-1] - k, floor(a[n-1] / 2) if x + 1 < 15 else 0)
    
#     # for i in range(n):
#     #     print(dp[i])

#     dp[n-1] = max(a[n-1] - k, floor(a[n-1]/2))

#     for i in range(n-2, -1, -1):
#         full = a[i] - k
#         half = floor(a[i]/2) + floor(dp[i+1] / 2 )

#         dp[i] = max(full + dp[i+1], half)
    
#     # for i in range(n-2, -1, -1):
#     #     for x in range(15):
#     #         # Option 1: Full pick
#     #         full_pick = a[i] - k + dp[i+1][x]
            
#     #         # Option 2: Half pick
#     #         if x + 1 < 15:
#     #             half_pick = floor(a[i] / 2) + dp[i+1][x+1] // 2
#     #         else:
#     #             half_pick = 0
            
#     #         dp[i][x] = max(full_pick, half_pick)
     
#     print(dp[0])
#     # print(dp[0][0])



######################################
# def max_points_dp(i, picked_half, n, k, produce, dp):
#     if i >= n:
#         return 0
    
#     if dp[i][picked_half] != -1:
#         return dp[i][picked_half]
    
#     if picked_half:
#         full_pick = (produce[i] // 2) - k + max_points_dp(i + 1, False, n, k, produce, dp)
#     else:
#         full_pick = produce[i] - k + max_points_dp(i + 1, False, n, k, produce, dp)
    
#     if picked_half:
#         half_pick = floor(produce[i] // 2 / 2) + max_points_dp(i + 1, True, n, k, produce, dp)
#     else:
#         half_pick = floor(produce[i] / 2) + max_points_dp(i + 1, True, n, k, produce, dp)
    
#     dp[i][picked_half] = max(full_pick, half_pick)
#     return dp[i][picked_half]

# def max_points(n, k, produce):
#     dp = [[-1] * 2 for _ in range(n)]
    
#     return max_points_dp(0, False, n, k, produce, dp)

# t = int(input())
# results = []

# for _ in range(t):
#     n, k = map(int, input().split())
#     produce = list(map(int, input().split()))
#     results.append(max_points(n, k, produce))

# for result in results:
#     print(result)

######################################

# def max_points_dp(i, x, n, k, produce, dp):
#     if i >= n:
#         return 0
    
#     if x >= 14:
#         return 0
    
#     if dp[i][x] != -1:
#         return dp[i][x]
    
#     full_pick = max(produce[i] // (2 ** x) - k, 0) + max_points_dp(i + 1, x, n, k, produce, dp)
    
#     half_pick = floor(produce[i] // (2 ** x) / 2) + max_points_dp(i + 1, x + 1, n, k, produce, dp)
    
#     dp[i][x] = max(full_pick, half_pick)
#     return dp[i][x]

# def max_points(n, k, produce):
#     dp = [[-1] * 14 for _ in range(n)]
    
#     return max_points_dp(0, 0, n, k, produce, dp)

# t = int(input())
# results = []

# for _ in range(t):
#     n, k = map(int, input().split())
#     produce = list(map(int, input().split()))
#     results.append(max_points(n, k, produce))

# for result in results:
#     print(result)


# def max_points_for_farmersam(n, k, produce):
#     max_fruits = max(produce)
#     max_halvings = 0
#     while max_fruits > 0:
#         max_fruits //= 2
#         max_halvings += 1
    
#     dp = [[0] * max_halvings for _ in range(n)]
    
#     for j in range(max_halvings):
#         dp[-1][j] = max(produce[-1] // (2 ** j) - k, produce[-1] // (2 ** (j + 1)))
    
#     for i in range(n - 2, -1, -1):
#         for j in range(max_halvings):
#             full_pick = produce[i] // (2 ** j) - k + dp[i + 1][j]
#             half_pick = produce[i] // (2 ** (j + 1)) + dp[i + 1][min(j + 1, max_halvings - 1)]
#             dp[i][j] = max(full_pick, half_pick)
    
#     return max(dp[0])

# t = int(input())
# results = []

# for _ in range(t):
#     n, k = map(int, input().split())
#     produce = list(map(int, input().split()))
#     results.append(max_points_for_farmersam(n, k, produce))

# for result in results:
#     print(result)


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [[0] * 15 for _ in range(n)]

    temp = a[-1]
    for x in range(15):
        dp[-1][x] = max(temp // 2, temp - k)
        temp //= 2

    for i in range(n - 2, -1, -1):
        temp = a[i]
        for j in range(15):
            
            full_pick = temp - k + dp[i + 1][j]
            half_pick = temp // 2 + dp[i + 1][min(15 - 1, j + 1)] 

            dp[i][j] = max(full_pick, half_pick)
            temp //= 2
    
    # for i in range(n):
    #     print(dp[i])
    
    print(dp[0][0])