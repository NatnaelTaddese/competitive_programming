n, m = map(int, input().split())
a = list(map(int, input().split()))

valid = 0

# prefix_sum = [0] *  (n + 1)

prefix_sum = 0
prefix_sum_freq = {0: 1} 

# for i in range(n):
#     prefix_sum[i + 1] = prefix_sum[i] + a[i]

# # print(prefix_sum)

# left = 1
# right = 1

# while(left < n + 1):
#     right = left
#     while right < n + 1:
#         if (prefix_sum[right] - prefix_sum[left -  1]) % m == 0:
#             valid += 1
#         right += 1
#     left += 1
# print(valid)

for i in range(n):
    prefix_sum = (prefix_sum + a[i]) % m
    complement = (prefix_sum - m) % m  
    valid += prefix_sum_freq.get(complement, 0) 
    prefix_sum_freq[prefix_sum] = prefix_sum_freq.get(prefix_sum, 0) + 1

print(valid)