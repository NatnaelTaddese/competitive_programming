# pairs = 0

# n = int(input())

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))


from collections import defaultdict

n = int(input())

arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
crr = list(map(int, input().split()))

dictionary = defaultdict( lambda : 0)

for i in range(n):
    # we do -1 because the array is 1-indexed
    dictionary[brr[crr[i] - 1]] += 1

count = 0
for number in arr:
    count += dictionary[number]

print(count)





# n = int (input())

# arr_a = list(map(int, input().split()))
# arr_b = list(map(int, input().split()))
# arr_c = list(map(int, input().split()))

# # Counting the frquency of each element in the array a
# frquency = {}
# for num in arr_a:
#     frquency[num] = frquency.get(num, 0) + 1

# #counting each
# possible_pairs = 0
# for j in range(n):
#     possible_pairs += frquency.get(arr_b[arr_c[j] - 1], 0)

# print(possible_pairs)