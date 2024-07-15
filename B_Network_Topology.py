from collections import defaultdict


n, m = map(int,input().split())

edges = []

for _ in range(m):
    a, b = map(int,input().split())
    edges.append([a, b])

# print(edges)

visited = [False for _ in range(n)]

adj_list = defaultdict(list)
for a, b in edges:
    adj_list[a].append(b)
    adj_list[b].append(a)

# print(adj_list)


degree_count = [0 for _ in range(n)]
for node in range(n):
    degree_count[node] = len(adj_list[node + 1])

# print(degree_count)
# buss

if degree_count.count(1) == 2 and degree_count.count(2) == n - 2:
    print("bus topology")


# ring 

elif degree_count.count(2) == n:
    print("ring topology")

# star

elif degree_count.count(1) ==  n - 1 and degree_count.count(n - 1) == 1:
    print("star topology")


else:
    print( "unknown topology")