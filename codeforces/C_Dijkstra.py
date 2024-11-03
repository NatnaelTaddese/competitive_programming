from collections import defaultdict
import heapq


n, m = map(int, input().split())
graph = defaultdict(list)
    
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

# print(graph)

    
def bfs(node):
    heap = [(0,[node])]
    visited = set()
    distances = {i: float('inf') for i in graph}
    distances[node] = 0
    result = [float('inf'), []]
    while heap:
        curr_weight, path = heapq.heappop(heap)
        curr = path[-1]
        if curr in visited:
            continue
        visited.add(curr)
        # if curr == n:
        #     return path
        # print(curr, path)
        
        for neighbor, weight in graph[curr]:
            # print(neighbor,path)
            
                
            distance = curr_weight + weight
            if neighbor == n and result[0] > distance:
                result = [distance, path + [neighbor]]
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance

                new_path = path[:] + [neighbor]
                heapq.heappush(heap,(distance, new_path))
    
        
    return " ".join(map(str, result[1])) if result[0] != float('inf') else '-1'


print(bfs(1))
