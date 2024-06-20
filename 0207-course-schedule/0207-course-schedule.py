class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.prereq = defaultdict(list)
        for u, v in prerequisites:
            self.prereq[u].append(v)

        self.stack = set()
        self.paths = set()
        
        def dfs(course):
            if course in self.paths:
                return False
            if course in self.stack:
                return True

            self.stack.add(course)
            self.paths.add(course)
            
            for req in self.prereq[course]:
                if not dfs(req):
                    return False
            
            self.paths.remove(course)
            return True
        
        for course in range(numCourses):
            if course not in self.stack:
                if not dfs(course):
                    return False
        
        return True
        

        