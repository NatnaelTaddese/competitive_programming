n, k = map(int, input().split())
h = list(map(int, input().split()))

min_index = 0
# min_sum = float('inf')

current_sum = sum(h[:k])
min_sum = current_sum

for i in range(k,n):
    current_sum = current_sum - h[i - k] + h[i]
    if current_sum < min_sum:
        min_sum = current_sum
        min_index = i - k + 1

print(min_index + 1)


# 1 2 6 1 1 7 1
# k : 3
# curr = 1 + 2 + 6