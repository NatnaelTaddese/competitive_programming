n, target = map(int, input().split())
arr = list(map(int, input().split()))

store = {}

for i, num in enumerate(arr):
    for j in range(i + 1, len(arr)):
        total = arr[i] + arr[j]
        if target - total in store:

            print(*store[target - total], i + 1, j + 1)
            exit()

for j in range(i):
    total = arr[i] + arr[j]
    store[total] = (i + 1, j + 1)

print("IMPOSSIBLE")