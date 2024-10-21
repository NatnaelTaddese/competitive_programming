n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cookies = []
remainders = []

for i in range(len(a)):
    cookies.append(b[i] // a[i])

mn_cookie = min(cookies)

for i in range(len(cookies)):
    remainders.append(b[i] - (a[i] * mn_cookie))


# print(cookies)
# print(mn_cookie,remainders)

for i in range(len(remainders)):
    if remainders[i] < a[i]:
        k -= a[i] - remainders[i]
        remainders[i] += a[i] - remainders[i]
    if k < 0:
        break
else:
    cookies = []
    for i in range(len(a)):
        cookies.append(remainders[i] // a[i])
    extra_cookies = min(cookies)
    mn_cookie += extra_cookies

print(mn_cookie)



"""
    3 - 2 = 1
    4 3 5 6
    11 12 14 20

sugar   11 - 4 = 7 - 4 = 3      - 4 = -1(1)
        12 - 3 = 9 - 3 = 6      - 3 = 3
        14 - 5 = 9 - 5 = 4      - 5 = -1(1)
        20 - 6 = 14 - 6 = 8     - 6 = 2
"""