n = int(input())
a = list(map(int, input().split()))

# swapped = False

# for i in range(n):
#     if a[i] != a[(2*n) - 1  - i]:
#         a[i], a[(2* n) - 1 - i] = a[(2*n) - 1 - i], a[i]
#         swapped = True
#         break


# if not swapped:
#     print(-1)
# else:
#     for i in a:
#         print(i, end=" ")

a = sorted(a)

# if len(a) < 4:
#     print(-1)
# elif a[0] == a[-1]:
#     print(-1)
# else:
#     for i in a:
#         print(i, end=" ")

if sum(a[:n]) == sum(a[n:]):
    print(-1)
else:
    for i in a:
        print(i, end=" ")