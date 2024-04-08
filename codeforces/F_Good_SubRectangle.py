n , m = map(int, input().split())

mtx = []

prefix_mtx = [[0] * (m + 1)] * (n + 1)

for _ in range(n):
    row = list(map(int, input().split()))
    mtx.append(row)

for i in range(1,n+1):
    for j in range(1, m+1):
        prefix_mtx[i][j] = prefix_mtx[i-1][j] + prefix_mtx[i][j - 1] - prefix_mtx[i-1][j-1] + mtx[i-1][j-1]

# DEBUG
        
print(prefix_mtx)

'''
0 1 0
0 1 0
0 1 0

'''

# brute force:
# calculate the area for every "c"?

max_area = 0

# for i in range(n):
#     for j in range(m):
#         for k in range(i,n):
#             for l in range(j,m):
#                 area = (k - i + 1) * (l - j + 1)
#                 count = 0
#                 for x in range(i, k + 1):
#                     for y in range(j, l + 1):
#                         if x < n and y < m:
#                             if mtx[x][y] == 1:
#                                 count += 1
#                 if area == 2 * count:
#                     max_area = max(max_area, area)

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                area = (k - i + 1) * (l - j + 1)
                count_ones = sum(mtx[x][y] for x in range(i, k + 1) for y in range(j, l + 1))
                if area == 2 * count_ones:
                    max_area = max(max_area, area)


print(max_area)







# max_area = 0
# c = 0

# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         # iterates over all possible top-left corners of the rectangle
#         for k in range(1, m + 1):
#             for l in range(k, m + 1):
#                 # finds the area and compare it with the prefix sum
                
#                 c = prefix_mtx[j][l] - prefix_mtx[j][k - 1] - prefix_mtx[i - 1][l] + prefix_mtx[i- 1][k - 1]
#                 area = (j - i + 1) * (l - k + 1)
#                 if area == 2 * c:
#                     max_area = max(max_area, area)


# print(max_area)

# or 
# 2D sliding window? 