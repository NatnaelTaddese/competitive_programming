for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    sorted_a = sorted(a)
    prefix_sum = [0] * n
    prefix_sum[0] = sorted_a[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + sorted_a[i]
    
    result = []

    def binary_search(arr,x):
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] <= x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    # print(sorted_a, prefix_sum)
    for i in range(n):
        score = a[i]
        # index of score in sorted_a
        # i = sorted_a.index(score)
        i = binary_search(sorted_a, score) - 1
        score = prefix_sum[i]

        while i < n - 1:
            if score >= sorted_a[i + 1]:
                score += sorted_a[i + 1]
                i += 1
            else:
                break
        result.append(i)

        
    print(*result)
