from collections import defaultdict
 
 
n = int(input())
 
edges = []
 
for _ in range(n - 1):
    a, b = map(int, input().split())
    edges.append([a, b])
 
 
adj_list = defaultdict(list)
for a, b in edges:
    adj_list[a].append(b)
    adj_list[b].append(a)
 
 
# def dfs(node, color, current_color, adj_list):
#     color[node] = current_color
#     for neighbor in adj_list[node]:
#         if color[neighbor] == -1:
#             if not dfs(neighbor, color, 1 - current_color, adj_list):
#                 return False
#         elif color[neighbor] == current_color:
#             return False
#     return True
 
 
 
# # print(adj_list)
 
# # possible = 0
 
# # for edge in adj_list:
 
# #     if len(adj_list[edge]) == 2:
# #         continue
 
# #     next_edge = edge + 1
 
# #     while( next_edge < n):
# #         if next_edge in adj_list and len(adj_list[next_edge]) == 1:
# #             possible += 1
# #             break
# #         else:
# #             next_edge += 2
 
 
# # print(possible)
 
 
 
 
 
# # color = [-1 for _ in range(n + 1)]
# # is_bipartite = True
 
# # for i in range(1, n + 1):
# #     if color[i] == -1:
# #         if not dfs(i, color, 0, adj_list):
# #             is_bipartite = False
# #             break
 
# # # this only checks if the tree is bipartite or not
 
# # if not is_bipartite:
# #     print(0)
# # else:
 
# #     set_blue = sum(1 for c in color if c == 0)
# #     set_red = n - set_blue
 
# #     # if it is bipartite that means every elemnt in the first set can match with the one in the second
 
# #     # u X v
# #     max_possible_edges = set_blue * set_red
# #     existing_edges = len(edges)
 
# #     print(max_possible_edges - existing_edges)
 
 
# def isBipartite(graph):
    
#     visited = [-1 for _ in range(n + 1)]
#     set1 = set()
#     set2 = set()
 
#     def dfs(node, depth):
#         # the node represents its depth
#         visited[node] = depth
 
#         if depth % 2 == 0:
#             set1.add(node)
#         else:
#             set2.add(node)
 
#         for neighbor in graph[node]:
#             # hasn't been visited
#             if visited[neighbor] == -1:
#                 if not dfs(neighbor, depth + 1):
#                     return False
#             # this means there is a cycle
#             # if it's even then it is bipartite
#             elif (depth - visited[neighbor]) % 2 == 0:
#                 return False
 
#         return True
 
#     # Check each component of the graph
#     for i in range(len(graph)):
#         if visited[i] == -1:
#             if not dfs(i, 0):
#                 return False , set1, set2
            
#     return True, set1, set2
 
# valid, blue, red = isBipartite(adj_list)
 
# if valid:
#     print(blue,red)
#     max_possible_edges = len(blue) * len(red)
#     existing_edges = len(edges)
 
#     print(max_possible_edges - existing_edges)
 
# else:
#     print(0)
 
 
def isBipartite(graph, n):
    visited = [-1 for _ in range(n + 1)]
    set1 = set()
    set2 = set()
 
    def dfs(node, depth):
        visited[node] = depth
 
        if depth % 2 == 0:
            set1.add(node)
        else:
            set2.add(node)
 
        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                if not dfs(neighbor, depth + 1):
                    return False
            elif (depth - visited[neighbor]) % 2 == 0:
                return False
 
        return True
 
    for i in range(1, n + 1):
        if visited[i] == -1:
            if not dfs(i, 0):
                return False, set(), set()
    
    return True, set1, set2
 
valid, blue, red = isBipartite(adj_list, n)
 
if valid:
    # print("Blue set:", blue)
    # print("Red set:", red)
    max_possible_edges = len(blue) * len(red)
    existing_edges = len(edges)
    print( max_possible_edges - existing_edges)
else:
    print(0)