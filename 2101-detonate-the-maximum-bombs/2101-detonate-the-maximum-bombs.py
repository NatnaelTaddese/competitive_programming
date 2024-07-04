class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        stack = []
        max_ = 0
        n = len(bombs)
        
        for i in range(n):
            visited = set()
            count = 1
            visited.add(i)
            stack.append(bombs[i])

            while stack:
                node = stack.pop()
                for j in range(n):
                    if j not in visited and (node[0] - bombs[j][0])**2 + (node[1] - bombs[j][1])**2 <= node[2]**2:
                        count += 1
                        stack.append(bombs[j])
                        visited.add(j)
            
            max_ = max(count, max_)
        
        return max_