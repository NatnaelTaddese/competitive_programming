class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        
        piles = [-x for x in piles]
        heapq.heapify(piles)
        
        for _ in range(k):
            curr = heapq.heappop(piles)
            curr = int(floor(curr / 2))

            heapq.heappush(piles,curr)
        

        result = 0

        for pile in piles:
            result += pile
        
        return -1 * result