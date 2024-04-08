n, m = map(int, input().split())
ones = []


mtx = []
valid_mtx = True

min_distance = m * n

for _ in range(n):
    row = list(map(str, input()))
    mtx.append(row)

    one = []
    one_found = False
    for i in range(m):
        if  row[i] == '1':
            one_found = True
            one.append(i + 1)
    ones.append(one)

    if  not one_found:
        valid_mtx = False
        break


if not valid_mtx:
    print(-1)
    exit()

# print(ones)

# ####### alternative approach
# for _ in range(n):
#     row = list(map(int, input().strip()))
#     ones.append([i + 1 for i, val in enumerate(row) if val == 1])
#     distinct = set(row)
#     if len(distinct) == 1:
#         print(-1)
#         exit()

# min_distance = m * n
# ######


for i in range(len(ones[0])):
    origin =  ones[0][i]

    curr_distance = 0

    for k in range(1, len(ones)):
        min_dis = m
        for one in ones[k]:
            distance = abs(origin - one)

            if distance == 0:
                continue
            
            if distance > m // 2:
                distance = abs(distance - m)
            min_dis = min(min_dis, distance)
            
            # print(min_dis, end = " ")
        curr_distance += min_dis

    # print("total: ", curr_distance)

    min_distance = min(min_distance, curr_distance)

    # print("minimum: ", curr_distance)

print(min_distance)

#######  second approach

# distances = {}
# for i in ones[0]:
#     distances[i] = [min(abs(i - j), m - abs(i - j)) for j in range(1, m + 1)]


# for i in range(len(ones[0])):
#     origin = ones[0][i]
#     curr_distance = 0

    
#     valid_rows = [row for row in range(1, n) if ones[row]]  
#     for k in valid_rows:
#         min_dis = min(distances[origin][j-1] for j in ones[k])
#         curr_distance += min_dis

#     min_distance = min(min_distance, curr_distance)

# print(min_distance)
