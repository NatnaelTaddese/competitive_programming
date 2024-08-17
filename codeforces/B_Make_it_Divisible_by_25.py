"""
for a number to be divisible by 25
so the last two digit of the number must be divisible by 25.

number that are divisible by 25 in range [1, 99] = [25, 50, 75]
"""

valid = [25, 50, 75]

ends = {5:(7,2),0:(5,0)}

for _ in range(int(input())):
    n = input()
    n = list(map(int, str(n)))
    # print(n)

    minimum_deletions = float('inf')

    for i in range(len(n) - 1, -1, -1):
        if n[i] in ends:
            for j in range(i - 1, -1, -1):
                if n[j] in ends[n[i]]:
                    deletions = (i - j - 1) + (len(n) - 1 - i)
                    minimum_deletions = min(minimum_deletions, deletions)
                    break
                    
    
    print(minimum_deletions) if minimum_deletions != float('inf') else print(len(n))