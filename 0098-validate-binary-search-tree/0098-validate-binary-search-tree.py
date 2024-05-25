# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isBST(self,node,lower=float('-inf'), upper=float('inf') ):
        if not node:
            return True
            
        if  node.val <= lower or  node.val >= upper:
            return False
        
        if not self.isBST(node.right,  node.val, upper):
            return False
        if not self.isBST(node.left, lower,  node.val):
            return False
        
        return True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        
        return self.isBST(root)