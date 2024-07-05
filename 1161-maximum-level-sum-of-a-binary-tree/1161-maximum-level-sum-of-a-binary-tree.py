# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque([(root, 1)])
    
        max_level = 1
        max_sum = root.val

        level_sum = defaultdict(int)

        while queue:
            curr, level = queue.popleft()

            if curr.left:
                queue.append((curr.left, level + 1))
                level_sum[level + 1] += curr.left.val
            
            if curr.right:
                queue.append([curr.right, level + 1])
                level_sum[level + 1] += curr.right.val
            
        for key, val in level_sum.items():
            if val > max_sum:
                max_level = key
                max_sum = val
        

        return max_level


            


        