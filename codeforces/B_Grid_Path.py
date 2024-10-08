from collections import deque

# def dfs(x, y, distance, n, m, k, visited):
#     if x == n and y == m:
#         if distance == k:
#             return True
#         return False
    
#     visited.add((x, y))

#     if y + 1 <= m and (x, y + 1) not in visited:
#         if dfs(x, y + 1, distance + x, n, m, k, visited):
#             return True
        
#     if x + 1 <= n and (x + 1, y) not in visited:
#         if dfs(x + 1, y, distance + y, n, m, k, visited):
#             return True
    
#     visited.remove((x, y))  
#     return False

def reach(n,m,k):
    # visited = set()
    # return "YES" if dfs(1, 1, 0, n, m, k, visited) else "NO"
    if min_cost(n, m) <= k <= max_cost(n, m):
        return "YES"
    else:
        return "NO"

def min_cost(n, m):
    return (m - 1) + (n - 1) * m
    (m - 1) + (n*m - m)
    (n*m - 1)

def max_cost(n, m):
    return (n - 1) + (m - 1) * n
    (n -1 ) + (n*m - n)
    (n*m - 1)
 



for _ in range(int(input())):
    n, m, k = map(int, input().split())
    # x, y = 1, 1

    # distance = abs(n - x) + abs(m - y)
    # distance = abs(n - x) *x + abs(m - 1) *y
    # print("distance", distance) 
    # if distance >= k:
    #     print("YES")
    # else:
    #     print("NO")
    print(reach(n, m, k))


# def bfs(n, m, k):
#     queue = deque([(1, 1, 0)])
#     visited = set((1,1))

#     while queue:
#         x, y, distance = queue.popleft()

#         if x == n and y == m:
#             if distance == k:
#                 return "YES"
            
#         if y + 1 < m and (x, y + 1) not in visited:
#             queue.append((x, y + 1, distance + x))
#             visited.add((x, y + 1))

        
#         if x + 1 <= n and (x + 1, y) not in visited:
#             queue.append((x + 1, y, distance + y))
#             visited.add((x + 1, y))
    

#     return "NO"

"""
(n*m - 1)
n,m
n-1,m
(n-1) *m - 1 ,m = 

[_,1,1,1,1,1]
[1,1,1,1,1,1]
[1,1,1,1,1,1]
[1,1,1,1,1,1]
[1,1,1,X,1,1]
[1,1,1,1,1,1]
[1,1,1,1,1,1]


() ()

"""