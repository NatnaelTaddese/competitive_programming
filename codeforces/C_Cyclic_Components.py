from collections import defaultdict


n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(n+1)]

total_cycles = 0

def bfs(start):
    stack = [(start, -1)]

    count = 0

    edge_count = 0

    while stack:
        node, parent = stack.pop()
        if visited[node]:
            continue

        visited[node] = True
        count += 1

        edge_count += len(graph[node])

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if visited[neighbor]:
                return False

            stack.append((neighbor,node))

    # Question: can two nodes be considered a cycle?
    return count >= 2

for node in range(1,n+1):
    if not visited[node]:
        if bfs(node):
            total_cycles += 1

print(total_cycles)