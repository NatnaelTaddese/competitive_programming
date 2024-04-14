s = input()
m = int(input())

n = len(s)

prefix_sum = [0] * (n + 1)

for i in range(1, n):
    if s[i] == s[i - 1]:
        prefix_sum[i] = prefix_sum[i - 1] + 1
    else:
        prefix_sum[i] = prefix_sum[i - 1]

# O(N)

# debug
# print(prefix_sum)

for _ in range(m):
    left, right = map(int, input().split())
    print(prefix_sum[right - 1] - prefix_sum[left - 1])

# O(M)