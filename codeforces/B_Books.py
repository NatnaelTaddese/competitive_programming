# n , t = map(int, input().split())
# books = list(map(int, input().split()))

# result = 0

# for i in range(n):
#     curr = 0
#     curr_t = t
#     for j in range(i,n):
#         if curr_t - books[j] >= 0:
#             curr += 1
#             curr_t -= books[j]
#             # print(j)
#         else:
#             break
#     result = max(result,curr)
# print(result)

n , t = map(int, input().split())
books = list(map(int, input().split()))

result = 0
curr_sum = 0
curr_t = t
i = 0

for j in range(n):
    curr_sum += books[j]
    while curr_sum > t and i <= j:
        curr_sum -= books[i]
        i += 1
    result = max(result, j - i + 1)

print(result)
