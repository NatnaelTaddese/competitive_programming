for _ in range(int(input())):
    n, m = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    arr_a.sort()
    arr_b.sort()

    # sliding window?

    max_diff = 0
    curr_diff = 0
    # for a in arr_a:
    #     left = 0
    #     right = m - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if arr_b[mid] < a:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
        
    #     if left < m:
    #         max_diff = max(max_diff, abs(a - arr_b[left]))
    #     if right  >= 0:
    #         max_diff = max(max_diff, abs(a - arr_b[right]))

    # print(max_diff)
    '''
    6 1 2 4
    3 5 1 7 2 3

    1 2 4 6
    1 2 3 3 5 7
    1 - 7, 2 - 5, 4 - 3, 2 - 3, 1 - 2   
    '''
    for i in range(n):
        curr_diff += abs(arr_a[i] - arr_b[i])

    max_diff = curr_diff

    for i in range(n, m):
        curr_diff -= abs(arr_a[i - n] - arr_b[i - n])  # Remove leftmost element from window
        curr_diff += abs(arr_a[i] - arr_b[i])          # Add rightmost element to window
        max_diff = max(max_diff, curr_diff)

    print(max_diff)
