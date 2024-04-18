# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(0,head)
        curr = head
        prev = dummy

        # # d -> 3 -> 2 -> 1 -> 5-> 

        while curr:
        #     iterator = dummy
            if curr.next and curr.next.val < curr.val:
                    # Finding the position to insert curr.next
                    while prev.next and prev.next.val < curr.next.val:
                        prev = prev.next

                    temp = prev.next
                    prev.next = curr.next
                    curr.next = curr.next.next
                    prev.next.next = temp

                    # Reset prev to dummy
                    prev = dummy
            else:
                curr = curr.next
        #     while iterator != curr:
        #         if curr.val < iterator.next.val:
        #             # adjust position
        #             temp = curr
        #             prev.next = curr.next
        #             curr.next = iterator.next
        #             iterator.next = curr

        #             # curr = temp
        #             curr = prev.next
        #             break
        #         iterator = iterator.next
            
        #     if not curr:
        #         break
        #     curr = curr.next
        #     prev = prev.next
        


        return dummy.next