difficulty, m = map(int,input().split())

problems = list(map(int, input().split()))

result = [0 for _ in range(m)]

quota = (difficulty * (difficulty + 1)) / 2

seen = dict()


for i in range(len(problems)):
    if problems[i] not in seen:
        seen[problems[i]] = seen.get(problems[i], 0) + 1

        # check again even if rating is between 1 and difficulty
        # coz for some reason test 3 is not passing
        if problems[i] > difficulty or problems[i] <= 0:
            continue

        else:
            quota -= problems[i]
        

        if quota == 0:
            result[i] = 1
            seen = dict()
            quota = (difficulty * (difficulty + 1)) / 2
    else:
        pass

answer = "".join(map(str,result))
print(answer)