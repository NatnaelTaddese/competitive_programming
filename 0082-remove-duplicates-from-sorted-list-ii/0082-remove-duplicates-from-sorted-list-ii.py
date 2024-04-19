# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0,head)
        prev = dummy
        curr = head

        # while curr and curr.next:
        #     while curr.next:
        #         if curr.val == curr.next.val:
        #             curr.next = curr.next.next
        #         else:
        #             break
            
        #     prev = curr.next
        #     if prev:
        #         curr = prev.next
        #     else:
        #         break

        # return head

        while prev.next:
            curr = prev.next
            isDuplicate = False
        #     while prev.next.next:
        #         if prev.next.val == prev.next.next.val:
        #             prev.next.next = prev.next.next.next
        #             isDuplicate = True
        #         else:
        #             break   
        #     prev = prev.next
            
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
                isDuplicate = True

            if isDuplicate:
                prev.next = curr.next
            else:
                prev = prev.next

        return dummy.next