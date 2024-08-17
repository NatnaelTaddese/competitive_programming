n, k, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a. sort()
b. sort()
print(a, ": " , b)
"""
[20, 100] :  [10, 40, 60, 80]
how can we evenly distribute the the people?

[10,[20], 40,((50)) 60, 80, [100]]


[11] :  [7, 15]
[7, ((10)), [11], 15]
"""

total_time = 0

i = n - 1
j = k - 1

while i >= 0:

    best_time = float('inf')
    best_key_index = -1

    while j >= 0:
        person = a[i]
        key = b[j]

        time = abs(person - key) + abs(key - p)

        if time < best_time:
            best_time = time
            best_key_index = j
        j -= 1
    
    total_time += best_time
    i -= 1

print(total_time)