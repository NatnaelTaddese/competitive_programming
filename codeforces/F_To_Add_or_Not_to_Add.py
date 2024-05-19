n , k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

# print(a)

mode = 0
number = a[0]

# for i in range(n - 1):
#     moves = k
#     j = i + 1
#     while moves > 0 and j < n:
#         moves -= a[i] - a[j]
#         if moves >= 0:
#             j += 1
    
#     distance = abs(j - i)

#     if distance > mode:
#         mode = distance
#         number = a[i]
#         # print(distance, number)



# using the two poninter approach

left = 0
curr = 0

for right in range(n):
    curr += a[right]

    while (right - left + 1) * a[right] - curr > k:
        curr -= a[left]
        left += 1
    
    if right - left + 1 > mode:
        mode = right - left + 1
        number = a[right]
        

print(mode, number)