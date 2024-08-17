"""
1 2 3 4
2 3 1 4
3 2 1 4
4 2 3 1

target: 2 3 1 4
"""

from collections import defaultdict, deque


for _ in range(int(input())):
    n, k = map(int, input().split())

    screenshots = []
    for _ in range(k):
        screenshots.append(list(map(int, input().split())))
    
    graph = defaultdict(list)

    in_degree = [0 for _ in range(n+1)]

    for screenshot in screenshots:
        # we skip the first person because they are the owner
        for i in range(2,n):
            u = screenshot[i - 1]
            v = screenshot[i]
            graph[u].append(v)
            in_degree[v] += 1
    
    # o(k(n))
    roots = []

    for i in range(1,n+1):
        if in_degree[i] == 0:
            roots.append(i)
    
    queue = deque(roots)
    count = 0

    while queue:
        player = queue.popleft()
        count += 1
        for neighbor in graph[player]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # o(k(n))
    
    if count == n:
        print("YES")
    else:
        print("NO")
