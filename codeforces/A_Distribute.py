n = int(input())
a = list(map(int, input().split()))

# 1 5 7 4 4 3
# 1 3 4 4 5 7

index_map = {}
for i, v in enumerate(a):
    if v in index_map:
        index_map[v].append(i + 1)
    else:
        index_map[v] = [i + 1]

a.sort()

left = 0
right = len(a) - 1

while left < right:
    print(index_map[a[left]].pop(0), index_map[a[right]].pop(0)) 
    left += 1
    right -= 1