# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # curr, parent, grandparent
        queue = deque([(root, None, None)])

        total = 0

        while queue:
            node, parent, grandparent = queue.popleft()

            if grandparent:
                if grandparent.val % 2 == 0:
                    total += node.val

            if node.left:
                queue.append((node.left, node, parent))
            if node.right:
                queue.append((node.right, node, parent))
            
        return total