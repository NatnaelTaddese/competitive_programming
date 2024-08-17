
"""
[1] : [0, 1]
YES
[2] : [0, 2]
NO
[1, 1, 2, 3, 5] : [0, 1, 2, 4, 7, 12]
YES
[1, 1, 2, 5, 7] : [0, 1, 2, 4, 9, 16]
NO
[1, 1, 1] : [0, 1, 2, 3]
YES
[1, 1, 1, 2, 4] : [0, 1, 2, 3, 5, 9]
YES

prefix sum: tells us the max sum we can get if we used all the subarray elements
"""
for _ in range(int(input())):
    n = int(input())  # the final c len
    a = list(map(int, input().split()))
    # a = sorted(a)
    a.sort()
    prefix = [0, 1]
    # print(a, end=' : ')
    for i in range(2, n + 1):
        prefix.append(prefix[i - 1] + a[i-1])

    # print(prefix)
    # curr = 1

    if a[0] > prefix[1]:
        print('NO')
        continue

    for i in range(1,n):
        if a[i] > prefix[i]:
            print('NO')
            break
    else:
        print('YES')
    
    # for i in range(n):
    #     if a[i] > curr:
    #         print('NO')
    #         break
    #     curr += a[i]
    # else:
    #     print('YES')
    
    