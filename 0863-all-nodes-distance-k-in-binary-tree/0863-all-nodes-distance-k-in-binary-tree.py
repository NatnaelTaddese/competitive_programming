# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        # bfs from the target to neighbors
        # until we reach k levels
        # combine all the nodes on that level and app
        graph = defaultdict(list)
        
        def build(node, parent):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                build(node.left, node)
                build(node.right, node)
        
        build(root, None)

        queue = deque([(target.val, 0)])
        visited = set([target.val])
        
        while queue:
            if queue[0][1] == k:
                return [node for node, dist in queue]
            
            node, dist = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        
        return []