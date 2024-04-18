# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tort = head
        rabbit = head

        idx = 0
        found = False

        while rabbit and rabbit.next:
            tort = tort.next
            rabbit = rabbit.next.next

            if rabbit == tort:
                found = True
                tort = head

                while rabbit != tort:
                    tort = tort.next
                    rabbit = rabbit.next
                    idx += 1
                break

        if found:
            return tort

        return None