class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        result = 0
        for operation in operations:
            if operation[1] == '+': # only checks the middle string
                result += 1
            else:
                result -= 1
        
        return result

        