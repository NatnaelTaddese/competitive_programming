from collections import deque


n = int(input())
a = list(map(int, input().split()))

answer = []

# card sorting, 
# patience sort
# sorting used to sort playing cards

for seq in a:
    l, r = 0, len(answer) - 1

    if len(answer) == 0:
        answer.append([seq])
        continue

    curr = 0
    while l <= r:
        mid = (l + r) // 2
        if answer[mid][-1] <= seq:
            curr = mid
            r = mid - 1
        else:
            l = mid + 1
    
    if answer[-1][-1] >= seq:
        answer.append([seq])
    else:
        answer[curr].append(seq)

for sequence in answer:
    print(" ".join(map(str, sequence)))
# queue = deque([0])
# unused = set(range(n))

# while queue:
#     init = queue.popleft()
#     if init not in unused:
#         continue
#     seq = [a[init]]
#     unused.remove(init)  

#     for i in list(unused):
#         if a[i] > seq[-1]:
#             seq.append(a[i])
#             unused.remove(i)  
#         else:
#             queue.append(i)
#     print(" ".join(map(str, seq)))




# used = [False] * n 

# def find_sub_array():
#     # sub_array = [a[start]]
#     sub_array = []
#     last_index = -float("inf")

#     for i in range(len(a)):
#         if not used[i] and a[i] >= last_index:
#             sub_array.append(a[i])
#             last_index = a[i]
#             used[i] = True

#     return sub_array

# while not all(used):
#     print(" ".join(map(str, find_sub_array())))

"""
[1, 3]      [2, 5, 4]
[1] [3]     [2] [5, 4]
                [5] [4]

1 3 
2

"""

# def merge(list1, list2):
#     i, j = 0, 0
#     n, m = len(list1), len(list2)
#     merged = [0 for _ in range(n + m)]
#     k = 0
    
#     prefix = 0

#     while (i < n and j < m):
#         if list1[i][0] <= list2[j][0]:
#             merged[k] = list1[i]
#             result[list1[i][1]] += prefix
#             i += 1
#         else:
#             merged[k] = list2[j]
#             prefix += 1
#             j += 1

#         k += 1

#     while (i < n):
#         merged[k] = list1[i]
#         result[list1[i][1]] += prefix
#         i+=1
#         k+=1
    
#     while (j < m):
#         merged[k] = list2[j]
#         j+=1
#         k+=1 
    
#     return merged

# def mergeSort(self,nums):
#     if len(nums) == 1:
#         return nums
#     mid = len(nums) // 2
#     left = mergeSort(nums[:mid])
#     right =mergeSort(nums[mid:])

#     return self.merge(left,right)

# n = int(input())
# nums = list(map(int, input().split()))

# indexes = [(nums[i], i) for i in range(len(nums))]
# result = [0 for _ in range(len(nums))]

# mergeSort(indexes)




# return self.result