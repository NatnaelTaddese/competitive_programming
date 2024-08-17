n = int(input())
weights = list(map(int, input().split()))

index = 0

# for i in range(n-1, 0, -1):
#     if weights[i] < weights[i-1]:
#         index = i
#         break

# find correct position
# frm = 0
# for i in range(index - 1, -1, -1):
#     if weights[index] >= weights[i]:
#         frm = i
#         break

visited = [False for _ in range(n)]
swaps = 0
# print(weights[frm:index])

# if len(set(weights[frm:index])) == 0:
#     print(0)
# else:
#     print(len(set(weights[frm:index])) - 1)

sorted_weights = sorted(weights)
index_map = {weight: i for i, weight in enumerate(sorted_weights)}


for i in range(n):
    if visited[i] or weights[i] == sorted_weights[i]:
        continue
    
    cycle_length = 0
    x = i
    
    while not visited[x]:
        visited[x] = True
        next_index = index_map[weights[x]]
        x = next_index
        cycle_length += 1
    
    if cycle_length > 0:
        swaps += (cycle_length - 1)
    
print(swaps)
