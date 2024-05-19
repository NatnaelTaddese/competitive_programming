n = list(input())
m = input()

zeroes = 0

ans = []
for ch in n:
    if ch == '0':
        zeroes += 1
        continue
    ans.append(int(ch))

ans.sort()

res = []

for num in ans:
    res.append(str(num))


# print(res)

r = ''

if zeroes != 0:
    zero = ['0'] * zeroes
    # res = res[0] + zero + res[1:len(res)]
    ans = ''
    ans += res[0]
    ans += ''.join(zero)
    ans += ''.join(res[1:len(res)])
    # print(ans)
    r = ans

else:
    r = ''.join(res)

if r == m:
    print("OK")
else:
    print("WRONG_ANSWER")



# i = 0

# found = False
# while i < len(ans):
#     if ans[i] == 0:
#         i+= 1
#     else:
#         found = True
#         break

# bob_found = False

# j = 0

# while j <len(m):
#     if m[j] == '0':
#         j+= 1
#     else:
#         bob_found = True
#         break


# if not found or not bob_found:
#     print('WRONG_ANSWER')

# else:
#     if ans[i] == int(m[j]):
#         print('OK')
#     else:
#         print("WRONG_ANSWER")