n, m = map(int, input().split())
l = list(map(int, input().split()))

prefix_sum = [0] *  (n + 1)

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + l[i - 1]

count = 1
curr_position = 0

for i in range(1, n + 1):
    # curr_position += l[i]
    if prefix_sum[i] <= m:
        count += 1
    else:
        break

print(count)