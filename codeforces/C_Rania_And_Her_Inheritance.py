n , m = map(int, input().split())
experts = []
rivals = dict(set())

possible_teams = [[]]

for _ in range(n):
    expert = input().strip()
    experts.append(expert)
    rivals[expert] = set()

for _ in range(m):
    a, b = input().split()
    rivals[a].add(b)
    rivals[b].add(a)


def valid(subset):
    for i in range(len(subset)):
        for j in range(i + 1, len(subset)):
            if subset[i] in rivals[subset[j]]:
                return False
    return True



def bactrack(index, curr_team):
    if index == n:
        if valid(curr_team):
            if len(curr_team) > len(possible_teams[0]):
                possible_teams[0] = curr_team[:]
        return
    
    # pick
    curr_team.append(experts[index])
    bactrack(index + 1, curr_team)

    # unpick
    curr_team.pop()
    bactrack(index + 1, curr_team)




bactrack(0, [])

print(len(possible_teams[0]))
for expert in sorted(possible_teams[0]):
    print(expert)


