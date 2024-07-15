from collections import defaultdict, deque


n = int(input())

tree = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False for _ in range(n + 1)]

sequence = list(map(int, input().split()))
i = 1


queue = deque([(sequence[0])])
visited[sequence[0]] = True


while queue and i < n:
    current = queue.popleft()

    for _ in range(len(tree[current])):
        for neighbor in tree[current]:
            if neighbor == sequence[i] and not visited[neighbor]:
                i += 1
                queue.append((neighbor))
                visited[neighbor] = True

if i == n:
    print("Yes")
else:
    print("No")