n = int(input())
books = list(map(int, input().split()))

# prefix_sum = [0] * (n + 1)

# for i in range(1, n+1):
#     prefix_sum[i] = prefix_sum[i - 1] + books[ i - 1]

# prefix_sum_from_back = [0] * (n + 1)
# for i in range(n - 1, -1 ,-1):
#     prefix_sum_from_back[i] = prefix_sum_from_back[i + 1] + books[i]

# # prefix_sum_from_back = prefix_sum_from_back[::-1]


# # debug:
# print(prefix_sum)
# print(prefix_sum_from_back)

# he = 0
# hr = 0
# if n % 2 == 0:
#     he = hr = n//2
# else:
#     he  = n // 2
#     hr  = he + 1


# print(prefix_sum_from_back[he],prefix_sum[hr])

hermoni_score = 0
hary_score = 0

# for i in range(1,n):
#     hermoni_score.append(max(books[i] + hary_score[i - 1], books[0], + hary_score[-1] ))
#     hary_score.append(max(books[i] + hermoni_score[i -1], books[-1] + hermoni_score[-1]))


# for i in range(n):
#     hermoni_score = max(hermoni_score, books[i] + prefix_sum_from_back[i + 1])
#     hary_score = max(hary_score, books[i] + prefix_sum_from_back[n-1])

# print(hermoni_score, hary_score)

left = 0
right = n - 1

while (left <= right):
    if books[left] > books[right]:
        hermoni_score += books[left]
        left += 1
    else:
        hermoni_score += books[right]
        right -= 1
    
    if left > right:
        break

    if books[left] > books[right]:
        hary_score += books[left]
        left += 1
    else:
        hary_score += books[right]
        right -= 1


print(hermoni_score, hary_score)
    



