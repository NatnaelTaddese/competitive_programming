from collections import Counter, defaultdict


n = int(input())
masses = list(map(int, input().split()))
mass_count = Counter(masses)

memo = dict()

m = list(mass_count.keys())
max_resource = 0

# print(mass_count)
###############################

def bactrack(mass_count, memo):

    state = tuple(sorted(mass_count.items()))
    if state in memo:
        return memo[state]

    if not mass_count:
        return 0
    
    max_resource = 0

    for mass in list(mass_count.keys()):
        curr = mass * mass_count[mass]

        #cant optimioze space for now,..
        new_count = mass_count.copy()

        del new_count[mass]
        if mass - 1 in new_count:
            del new_count[mass - 1]
        if mass + 1 in new_count:
            del new_count[mass + 1]
        
        curr += bactrack(new_count, memo)
        max_resource = max(max_resource, curr)
    
    memo[state] = max_resource
    return max_resource


for mass in m:
    curr = mass * mass_count[mass]
    for other in m:
        if other == mass or other == mass + 1 or other == mass - 1:
            continue
        curr += (mass_count[other] * other)

    max_resource = max(max_resource, curr)


max_resource = bactrack(mass_count, memo)

#########################################
# freq = defaultdict(int)

# for mass in masses:
#     freq[mass] += mass

# dp = dict()

# sorted_masses = sorted(freq.keys())

# dp[sorted_masses[0]] = freq[sorted_masses[0]]

# if len(sorted_masses) > 1:
#     dp[sorted_masses[1]] = max(freq[sorted_masses[0]], freq[sorted_masses[1]])

# for i in range(2, len(sorted_masses)):
#     mass = sorted_masses[i]
#     dp[mass] = max(dp[sorted_masses[i - 1]], dp[sorted_masses[i - 2]], freq[mass])

# print(max(dp.values()))

print(max_resource)


