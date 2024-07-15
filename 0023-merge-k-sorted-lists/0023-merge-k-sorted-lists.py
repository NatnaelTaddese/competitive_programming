# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        dummy = ListNode(0)

        curr = dummy

        for lst in lists:
            if lst:
                heapq.heappush(heap, (lst.val, lst))
        
        while heap:
            val, node = heappop(heap)
            curr.next = node

            if node.next:
                heappush(heap,  (node.next.val, node.next))
            
            curr = curr.next
        
        return dummy.next
        