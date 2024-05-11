# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head
    
        # Dummy node 
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        
        for _ in range(left - 1):
            prev = prev.next
        
        
        curr = prev.next
        next_node = curr.next
        
        # Reverse the sublist
        for _ in range(right - left):
            temp = next_node.next
            
            next_node.next = curr
            curr = next_node
            next_node = temp
        
        # Connect to original
        prev.next.next = next_node
        prev.next = curr
        
        return dummy.next
        