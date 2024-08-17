n = int(input())
a = list(map(int, input().split()))

# prefix = [0] * (n + 1)

max_len = 1
curr = 1

for i in range(1, n):
    if a[i] > a[i - 1]:
        # prefix[i+1] = prefix[i - 2] + 1
        curr += 1
        max_len = max(max_len, curr)
    else:
        # prefix[i+1] = prefix[i - 2]
        curr = 1

# print(max(prefix))
print(max_len)