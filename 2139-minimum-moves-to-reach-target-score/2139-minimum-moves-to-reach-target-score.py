class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        moves = 0
        num = target
        
        # while target > 1:
        #     if target % 2 == 0 and maxDoubles > 0:
        #         target //= 2
        #         maxDoubles -= 1
        #     elif target % 2 == 1:
        #         target -= 1
        #     else:
        #         target -= 1
            
        #     moves += 1
        while num != 1 and maxDoubles > 0:
            if num % 2 != 0:
                num -= 1
                moves += 1
            else:
                num //= 2
                moves += 1
                maxDoubles -= 1

        moves += (num - 1)

        
        return moves