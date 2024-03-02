# difficulty, m = map(int,input().split())

# problems = list(map(int, input().split()))

# result = [0 for _ in range(m)]

# quota = (difficulty * (difficulty + 1)) / 2

# seen = dict()

# for i in range(len(problems)):
#     if problems[i] not in seen:
#         seen[problems[i]] = seen.get(problems[i], 0) + 1

#         if problems[i] > difficulty or problems[i] <= 0:
#             continue

#         else:
#             quota -= problems[i]
        

#         if quota == 0:
#             result[i] = 1
#             seen = dict()
#             quota = (difficulty * (difficulty + 1)) / 2
#     else:
#         pass

# answer = "".join(map(str,result))
# print(answer)

n, m = map(int, input().split())
problems = list(map(int, input().split()))

pool = {}
quota = 0

for i in range(m):
    # Adds each question to the pool
    pool [problems[i]] = pool.get(problems[i], 0) + 1
    if pool [problems[i]] == 1:
        quota += 1

    if quota == n:
        for i in range(1, n + 1):
            pool[i] -= 1
            if pool[i] == 0:
                quota -= 1
        print(1, end="")
    else:
        print(0, end="")