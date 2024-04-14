n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# a.sort(reverse=True)
# b.sort(reverse=True)

# i = 0
# j = 0

result = []
# a_seen = dict()
# b_seen = dict()

# solved = True

# while i < n and j < m:
#     if a[i] == b[j]:
#         result.append(a[i])
#         i += 1
#         j += 1
#         while i < n and a[i] in a_seen:
#             i += 1
#         while j < m and b[j] in b_seen:
#             j += 1
#         continue

#     elif a[i] > b[j]:
#         cursor = j + 1
#         found = False
#         while cursor < m:
#             if b[cursor] + b[j] == a[i]:
#                 b_seen[cursor] = b_seen.get(cursor, 0) + 1
#                 result.append(a[i])
#                 i += 1
#                 j += 1
#                 while i < n and a[i] in a_seen:
#                     i += 1
#                 while j < m and b[j] in b_seen:
#                     j += 1
#                 found = True
#                 break
#             else:
#                 cursor += 1
#                 while cursor < m and b[cursor] in b_seen:
#                     cursor += 1
#         if not found:
#             solved = False
#             break
#     else:
#         cursor = i + 1
#         found = False
#         while cursor < n:
#             if a[cursor] + a[i] == b[j]:
#                 a_seen[cursor] = a_seen.get(cursor, 0) + 1
#                 result.append(b[j])
#                 i += 1
#                 j += 1
#                 while i < n and a[i] in a_seen:
#                     i += 1
#                 while j < m and b[j] in b_seen:
#                     j += 1
#                 found = True
#                 break
#             else:
#                 cursor += 1
#                 while cursor < n and a[cursor] in a_seen:
#                     cursor += 1
#         if not found:
#             solved = False
#             break

# if not solved:
#     print(-1)
# else:
#     print(len(result))


a_i = 0
a_j = n - 1

b_i = 0
b_j = m - 1


while(a_i < a_j and  b_i < b_j):
    if a[a_i] == b[b_i]:
        result.append(a[a_i])
        a_i += 1
        b_i += 1
    elif a[a_j] == b[b_j]:
        result.append(a[a_j])
        a_j -= 1
        b_j -= 1

    else:
        a_sum = 0
        b_sum = 0
        found  = False
        a_l, a_r, b_l, b_r =  a_i, a_j, b_i, b_j

        while(a_l < a_r and b_l < b_r):
            if  a[a_l] + a[a_r] == b[b_l]:
                a_sum +



