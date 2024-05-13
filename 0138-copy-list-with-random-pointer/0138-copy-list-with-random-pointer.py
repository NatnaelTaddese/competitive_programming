"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
            
        mapping = {}
        curr = head


        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            new_node = mapping[curr]
            # new_node.next = mapping.get(curr.next)
            # new_node.random = mapping.get(curr.random)
            new_node.next = mapping.get(curr.next)
            new_node.random = mapping.get(curr.random)
            curr = curr.next
        
        
        return mapping[head]