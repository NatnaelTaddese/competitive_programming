# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()

        curr = head
        remainder = 0
        # while l1 and l2:
        #     res = l1.val + l2.val + remainder

        #     curr.val = (res % 10)
        #     curr.next = ListNode()
        #     curr = curr.next
        #     remainder = res - (res % 10)

        #     l1 = l1.next
        #     l2 = l2.next

        while l1 or l2 or remainder:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            res = val1 + val2 + remainder

            curr.val = res % 10
            remainder = res // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            if l1 or l2 or remainder:
                curr.next = ListNode()
                curr = curr.next

        
        # # handle remaining

        # if l1:
        #     curr = l1
        # elif l2:
        #     curr = l2
        # else:
        #     return head
        
        # while remainder != 0 and curr:
        #     res = curr.val + remainder
        #     curr.val += res % 10
        #     curr = curr.next
        #     remainder = res - (res % 10)
        
        return head

        