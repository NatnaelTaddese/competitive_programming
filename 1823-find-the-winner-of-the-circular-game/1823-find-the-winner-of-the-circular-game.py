class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        friends = [i for i in range(1,n + 1)]
        position = 0
        remaining = n

        while( remaining != 1):
            position = (position + (k - 1)) % remaining
            friends.pop(position)
            remaining -= 1
        
        return friends[0]

