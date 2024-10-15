n = int(input())
a = list(map(int, input().split()))

chunk_a = []
chunk_b = []


"""
3 1 4
5 2 6

3 1 4 5 2 6

3 1
4 
5 2
6

[2, 1, 2, 1]

"""
used = set()

i = 0
while i < 2 * n:
    if a[i] in used:
        i += 1
        continue

    chunk_a.append(a[i])
    used.add(a[i])

    found = False
    for j in range(i + 1, 2 * n):
        if a[j] not in used:
            # if a[j]
            chunk_b.append(a[j])
            used.add(a[j])
            found = True
            break

    if not found:
        print(-1)
        exit()

    i += 1


print(" ".join(map(str, chunk_a)))
print(" ".join(map(str, chunk_b)))



"""
Output
3 1 2
4 5 6
Checker Log
wrong answer After merging, contestant 2-th element is 2 while the original array is 4
"""