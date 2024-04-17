# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = dict()

        curr = head

        while curr:
            if curr in seen:
                return True
            
            seen[curr] = 1
            curr = curr.next
        
        return False
        