# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        
        Result = []
        

        Result.extend(self.postorderTraversal(root.left))
        Result.extend(self.postorderTraversal(root.right))
        Result = Result + [root.val]

        
        # same as pre-order DFS but the positioning is different, the root note goes after left and right

        return Result
        