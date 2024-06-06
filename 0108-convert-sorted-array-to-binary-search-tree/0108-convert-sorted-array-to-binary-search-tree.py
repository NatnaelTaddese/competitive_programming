# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        def helper(left, right):
            if left > right:
                return None
            
            center = (left + right) // 2
            node = TreeNode(nums[center])
            node.left = helper(left, center - 1)
            node.right = helper(center + 1, right)
            
            return node
        
        return helper(0, len(nums) - 1)
        # if not nums:
        #     return None

        # center = len(nums) // 2
        
        # return TreeNode(
        #     nums[center],
        #     self.sortedArrayToBST(nums[:center]),
        #     self.sortedArrayToBST(nums[center + 1:])
        # )