from collections import defaultdict,  deque


n,m = map(int,input().split())

cats = list(map(int,input().split()))
edges = []

for _ in range(n - 1):
    u,v = map(int,input().split())
    edges.append([u,v])


tree = defaultdict(list)

for edge in edges:
    tree[edge[0]].append(edge[1])
    tree[edge[1]].append(edge[0])

# def dfs(node,parent,consecutive_cats):
#     #dfs
#     if cats[node - 1] == 1:
#         consecutive_cats += 1
#     else:
#         consecutive_cats = 0

#     if consecutive_cats > m:
#         return 0
    
#     is_leaf = True
#     total_restaurants = 0

#     for neighbor in tree[node]:
#         if neighbor != parent:
#             is_leaf = False
#             total_restaurants += dfs(neighbor,node,consecutive_cats)


#     if is_leaf:
#         return 1
    
#     return total_restaurants 


def bfs(start_node):
    queue = deque([(start_node, -1, 0)])  # (node, parent, consecutive_cats)
    total_restaurants = 0
    
    while queue:
        node, parent, consecutive_cats = queue.popleft()
        
        if cats[node - 1] == 1:
            consecutive_cats += 1
        else:
            consecutive_cats = 0
        
        if consecutive_cats > m:
            continue
        
        is_leaf = True
        
        for neighbor in tree[node]:
            if neighbor != parent:
                is_leaf = False
                queue.append((neighbor, node, consecutive_cats))
        
        if is_leaf:
            total_restaurants += 1
    
    return total_restaurants


# print(dfs(1,-1,0))

print(bfs(1))
