for _ in range(int(input())):

    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    count = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % x == 0 and (a[i] - a[j]) % y == 0:
                count += 1
    
    print(count)



# from collections import Counter

# def count_beautiful_pairs(n, x, y, a):
#     # Preprocess array to count elements divisible by x and y
#     count_x = Counter(ai % x for ai in a)
#     count_y = Counter(ai % y for ai in a)

#     # Initialize counter for beautiful pairs
#     beautiful_pairs = 0

#     for i in range(n):
#         for j in range(i+1, n):
#             # Check if both conditions are satisfied
#             if (a[i] + a[j]) % x == 0 and (a[i] - a[j]) % y == 0:
#                 beautiful_pairs += 1

#     return beautiful_pairs

# t = int(input())

# for _ in range(t):
#     n, x, y = map(int, input().split())
#     a = list(map(int, input().split()))
#     print(count_beautiful_pairs(n, x, y, a))


