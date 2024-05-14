class Solution(object):
    def add(self,num1,num2):
        return num1 + num2
    
    def subs(self,num1,num2):
        return num1 - num2
    
    def mult(self,num1,num2):
        return num1 * num2
    
    def div(self,num1,num2):
        # division by zero
        if num2 == 0:
            return 0
        if num1 * num2 < 0:
            return -(-num1 // num2)
        else:
            return num1 // num2
        
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operations = {"+": self.add, "-": self.subs, "*": self.mult, "/": self.div}

        for token in tokens:
            if token in operations.keys():
                second_num = int(stack.pop())
                first_num = int(stack.pop())
                result = operations[token](first_num, second_num)
                stack.append(result)
            else:
                stack.append(token)
        
        return int(stack[-1])
