# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))

#     c = a.copy()
#     swaps = 0
#     swaps2 = 0

#     if a == b:
#         print(swaps)
#         continue

#     for i in range(len(a) - 2):


#         cursor = i + 1
#         while(cursor < len(a) - 1):
#             if a[cursor] == b[i]:
#                 # print(a)
#                 swaps += 1
#                 while(cursor > i):
#                     a[cursor], a[cursor - 1] = a[cursor - 1], a[cursor]
#                     cursor -= 1
#                 break
#             else:
#                 cursor  += 1
        
#         # while(cursor > 0):
#         #     if a[cursor] == b[i]:
                
#         #         a[cursor], a[i] = a[i], a[cursor]
#         #         swaps += 1
#         #         break
#         #     else:
#         #         # a[cursor], a[cursor - 1] = a[cursor - 1], a[cursor]
#         #         cursor -= 1
        
#     for i in range(n-1,0,-1):
#         if b[i] == c[i]:
#             continue
        
#         cursor = i - 1
#         while(cursor > -1):
#             if c[cursor] == b[i]:
#                 swaps2 += 1
#                 while(cursor < i):
#                     c[cursor], c[cursor + 1] = c[cursor + 1], c[cursor]
#                     cursor += 1
#                 # print(c)
#                 break
                
#             else:
#                 cursor  -= 1
#     # print(min(swaps, swaps2))
#     print(swaps)

# 4 5 1 2 3
# 4 5 1 2 3

# 2
# 5 6 1 8 4 2 7 3
# 5 6 1 4 8 2 7 3  
    


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i = n - 1
    j = n - 1
    while i >= 0:
        if a[i] != b[j]:
            i -= 1
        else:
            i -= 1
            j -= 1
    print(j + 1)
