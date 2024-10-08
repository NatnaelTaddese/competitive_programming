# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        result = []
        
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        
        result.sort()

        ans = ListNode(result[0])
        curr = ans

        for val in result[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        
        return ans