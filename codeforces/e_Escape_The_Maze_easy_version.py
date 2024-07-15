from collections import defaultdict, deque


for _ in range(int(input())):
    n, k = map(int, input().split())
    friends = list(map(int, input().split()))

    maze = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        maze[u].append(v)
        maze[v].append(u)

    
    queue = deque([(1,friends)])
    player_visited = set()
    player_visited.add(1)

    friends_visited = [ set() for _ in range(k)]

    while queue:
        room, curr_friends = queue.popleft()

        if room in curr_friends:
            continue
        
        for neighbor in maze[room]:
            if neighbor not in player_visited:
                player_visited.add(neighbor)
                queue.append((neighbor, curr_friends))
                
