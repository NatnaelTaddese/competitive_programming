# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        # root_node = TreeNode(root)

        # curr = deque([])
        # paths = []
        # curr.append([root.val])
        # result =

        # while curr:

        #     for i in range(len(curr)):
        #         if curr.left:
        #             curr.append(curr.left)
        #         if curr.right:
        #             curr.append(curr.right)

        prefix_sum_counts = defaultdict(int)

        prefix_sum_counts[0] = 1


        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum += node.val
            
            path_count = prefix_sum_counts[current_sum - targetSum]
            
            prefix_sum_counts[current_sum] += 1
            
            path_count += dfs(node.left, current_sum)
            path_count += dfs(node.right, current_sum)
            
            # Backtrack
            prefix_sum_counts[current_sum] -= 1
            
            return path_count
        

        prefix_sum_counts = defaultdict(int)

        prefix_sum_counts[0] = 1


        return dfs(root, 0)
            



