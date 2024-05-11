# musicians = []
musicians = dict()

for _ in range(int(input())):
    x, y = map(int,input().split())
    musicians[y] = musicians.get(y, 0) + x
    # for _ in range(x):
    #     musicians.append(y)


# musicians.sort()

#sort the dictionary
sorted_musicians = dict(sorted(musicians.items(), key= lambda item: item[0]))


# print(sorted_musicians)

musicians = list(sorted_musicians.keys())
freq = list(sorted_musicians.values())

left = 0
right = len(musicians) - 1

total_time = musicians[left] + musicians[right]

while left <= right:
    if freq[left] <= 0:
        left += 1
        continue
    if freq[right] <= 0:
        right -= 1
        continue

    # print(musicians[left], musicians[right])

    total_time = max(total_time, musicians[left] + musicians[right])
    freq[left] = max(0, freq[right] - freq[left])
    freq[right] = max(0, freq[left] - freq[right])
    # print(freq)

    



# while left < right:
#     total_time = min( total_time, musicians[left] + musicians[right])
#     left += 1
#     right -= 1

# while 

print(total_time)