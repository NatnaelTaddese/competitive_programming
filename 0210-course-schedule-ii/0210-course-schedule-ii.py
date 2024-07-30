class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        requirements = {i: 0 for i in range(numCourses)}
        result = []
        queue = deque()

        for u, v in prerequisites:
            graph[v].append(u)
            requirements[u] += 1
        
        # Find the courses with no prerequisites
        for course in range(numCourses):
            if requirements[course] == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            result.append(course)

            for neighbor in graph[course]:
                requirements[neighbor] -= 1

                if requirements[neighbor] == 0:
                    queue.append(neighbor)
                
        if len(result) != numCourses:
            return []
        
        return result