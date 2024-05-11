# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    # helper function
    def push_to_stack(self, l, stack):
            while l:
                stack.append(l.val)
                l = l.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        stack1 = []
        stack2 = []
        
        self.push_to_stack(l1, stack1)
        self.push_to_stack(l2, stack2)
        
        carry = 0
        result_head = None
        
        # Pop digits and add
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            
            #node to store the result
            new_node = ListNode(total % 10)
            new_node.next = result_head
            result_head = new_node
        
        return result_head
        