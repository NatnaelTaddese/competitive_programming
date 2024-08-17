class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """

        in_degree = [0 for _ in range(n)]
        for child in leftChild + rightChild:
            if child != -1:
                in_degree[child] += 1
        
        root = None
        
        for i in range(n):
            if in_degree[i] == 0:
                if root is not None:
                    return False
                root = i
            elif in_degree[i] > 1:
                return False

        print(in_degree, "root:", root)
        # return True

        visited = set()
        def dfs(node):
            if node != -1 and node not in visited:
                visited.add(node)
                # print(visited, node)
                if not node:
                    dfs(leftChild[0])
                else:
                    dfs(leftChild[node])
                if not node:
                    dfs(rightChild[0])
                else:
                    dfs(rightChild[node])
                # dfs(rightChild[node])
        
        dfs(root)
        return len(visited) == n