# n, m, x, y = map(int, input().split())

# barcode = []

# for i in range(n):
#     row = []
#     s = input()
#     for char in s:
#         row.append(char)
#     barcode.append(row)



# # print(barcode)
# barCol = dict()


# # for each column, count the number of '#' characters
# for i in range(m):
#     for j in range(n):
#         if barcode[j][i] == '#':
#             barCol[i] = barCol.get(i, 0) + 1

# print(barCol)


# def bactrack(i, isWhite, state, pixels):
#     if i == m:
#         return pixels
    
#     #
#     if isWhite:




# total = min(bactrack(i,True, 1,0), bactrack(i, False,1,0))

n, m, x, y = map(int, input().split())
barcode = [input().strip() for _ in range(n)]

white = [0 for _ in range(m)]
black = [0 for _ in range(m)]

for j in range(m):
    for i in range(n):
        if barcode[i][j] == '.':
            white[j] += 1
        else:
            black[j] += 1

dp = [[float('inf')] * 2 for _ in range(m + 1)]
dp[0][0] = dp[0][1] = 0

for i in range(1, m + 1):
    for j in range(x, y + 1):
        if i - j >= 0:
            white_cost = sum(white[i-j:i])
            black_cost = sum(black[i-j:i])
            dp[i][0] = min(dp[i][0], dp[i-j][1] + white_cost)
            dp[i][1] = min(dp[i][1], dp[i-j][0] + black_cost)

result = min(dp[m][0], dp[m][1])
print(result)