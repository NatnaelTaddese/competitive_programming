# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # brute force
        # # skip : get a sense of the size
        # connect the tail to the head
        # rotate array
        # break the tail and head

        curr = head
        
        size = 0
        while curr:
            size += 1
            curr = curr.next

        
        if k == 0 or size == 0:
            return head
        # 0 1 2 0 1 2 0 1 2
        # move = abs(size - k)
        move = k % size
        if move == 0:
            return head
                
        # while move != 0:
        #     curr = curr.next
        #     if not curr.next:
        #         curr = head    
        #     move -= 1
        # end = curr
        # while size != 0:
        #     end = end.next
        #     if not end.next:
        #         end = head
            
        #     size -= 1
        
        # end.next = None
        fast = head
        slow = head
        for _ in range(move):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Perform the rotation here
        new_head = slow.next
        slow.next = None
        fast.next = head
        
        return new_head





        