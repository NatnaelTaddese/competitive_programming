from collections import defaultdict, deque


n = int(input())

repost_tree = defaultdict(list)

for _ in range(n):
    name1, action, name2 = input().split(" ")
    name2 = name2.lower()
    name1 = name1.lower()
    repost_tree[name2].append(name1)


queue = deque([("polycarp", 1)])  
max_depth = 1


while queue:
    current, depth = queue.popleft()

    for neighbor in repost_tree[current]:
        queue.append((neighbor, depth + 1))

        max_depth = max(max_depth, depth + 1)

print(max_depth)