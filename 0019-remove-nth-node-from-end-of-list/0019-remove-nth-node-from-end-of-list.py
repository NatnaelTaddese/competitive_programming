# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # Brute Force
        # get a sense of the length of the linked list and then go through it again to remove it
        size = 0

        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        to_remove = size - n

        if to_remove == 0:
            return head.next

        curr = head
        for _ in range(to_remove - 1):
            curr = curr.next
        
        curr.next = curr.next.next


        return head
        
