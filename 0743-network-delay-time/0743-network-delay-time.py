class Solution:
    def dijkstra(self, n, graph, start):
        distances = {node: float('inf') for node in range(1,n+1)}
        distances[start] = 0
        visited = set()
        heap = [(0, start)]

        while heap:
            curr_distance, curr_node = heapq.heappop(heap)

            if curr_node in visited:
                continue

            visited.add(curr_node)

            for neighbor, weight in graph[curr_node]:
                distance = curr_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        total = self.dijkstra(n, graph, k)
        print(total)
        if float('inf') in total.values():
            return -1
        
        return max(total.values())

        