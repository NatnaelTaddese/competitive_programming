# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))

#     difference = 0

#     a.sort()
#     b.sort()

#     if n == 1:
#         print(abs(a[0] - max(b)))
#         continue

#     j = m - 1
#     for i in range((len(a) // 2) - 1 , - 1, -1):
#         difference += abs(a[i] - b[j])
#         # print(a[i] , b[j])
#         j -= 1
    
#     j = 0
#     for i in range(len(a) - 1, (len(a) // 2) - 1 ,-1):
#         difference += abs(a[i] - b[j])
#         j+= 1
#         # print(a[i] , b[j])


#     print(difference)



for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    difference = 0

    a.sort()
    b.sort()

    if n == 1:
        print(abs(a[0] - b[-1]))
        continue

    j = m - 1
    for i in range((len(a) // 2) - 1, -1, -1):
        difference += abs(a[i] - b[j])
        j -= 1

    j = 0
    for i in range(len(a) // 2, len(a)):
        difference += abs(a[i] - b[j])
        j += 1

    print(difference)


    # 6 1 2 4
    # 1 5 7 2


    # 1 2 4 6
    # 5 7 2 1


    # 1 2 3 3 5 7



# 1 2 3 4 5
# 5 4 3 2 1


# 1 2 3 4 5

