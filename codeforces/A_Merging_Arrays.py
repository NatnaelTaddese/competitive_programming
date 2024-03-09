n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = 0

result = []

while (i < n and j < m):
    if (a[i] < b[j]):
        result.append(a[i])
        i += 1
    elif(a[i] > b[j]):
        result.append(b[j])
        j += 1
    else:
        result.append(a[i])
        result.append(b[j])
        i += 1
        j += 1

while i < n:
    result.append(a[i])
    i += 1

while j < m:
    result.append(b[j])
    j += 1

for r in result:
    print(r, end=" ")
