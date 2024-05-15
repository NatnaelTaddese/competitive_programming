# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        Result = [root.val]

        # since we are doing DFS, we prioritize the left most node
        # so we go throug the left until we found None, and proceed
        # to the left

        Result.extend(self.preorderTraversal(root.left))

        Result.extend(self.preorderTraversal(root.right))
    
        return Result
        