# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def dfs(node, min_val, max_val):
            if not node:
                return max_val - min_val
            
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            
            left_diff = dfs(node.left, min_val, max_val)
            right_diff = dfs(node.right, min_val, max_val)
            
            return max(left_diff, right_diff)
        
        return dfs(root, root.val, root.val)