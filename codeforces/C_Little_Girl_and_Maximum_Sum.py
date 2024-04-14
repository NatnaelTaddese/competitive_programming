from collections import Counter

n , q = map(int, input().split())

a = list(map(int, input().split()))

a.sort(reverse=True)

prefix_sum = [0] *  (n + 1)

for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + a[i]

result = 0

max_sum = 0

# prefix_sum = prefix_sum[::-1]
# debug
# print(prefix_sum)

# queries = []
left_indexes = []
right_indexes = []

for _ in range(q):
    left, right = map(int, input().split())
    # curr_sum = prefix_sum[right] - prefix_sum[left - 1]
    # result += prefix_sum[right] - prefix_sum[left - 1]
    # max_sum = max(max_sum, curr_sum)
    # print(prefix_sum[right], ":",prefix_sum[left])

    left_indexes.append(left)
    right_indexes.append(right)

# print(result)

left = Counter(left_indexes)
right = Counter(right_indexes)

most_left = max(left.values())



# debug
print(left, right)







# 5 2 4  1  3
# 5 7 11 12 15
# 15 12 11 7 5


# 15 + 23 + 23

# 5 3 2
# 5 8 10
# 8 + 5 + 10