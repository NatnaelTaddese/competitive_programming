# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rabbit = head
        tort = head

        steps = 1

        # while rabbit:
        #     tort = tort.next
        #     for _ in range(steps):
        #         if not rabbit:
        #             break
        #         rabbit = rabbit.next
            
        #     steps += 1

        # return tort
        # this failed because it gives the prev node if it's even and the next if it's odd
        # and we dont have a sense of size to determine if its even or od

        while rabbit and rabbit.next:
            tort = tort.next
            rabbit = rabbit.next.next

        return tort
        