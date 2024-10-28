class Solution:
    def findMinMax(self, nums:list[int]) -> (int, int):
        mn, mx = float('inf'), 0
        for num in nums:
            mn = min(num, mn)
            mx = max(num, mx)
        
        return mn, mx

    def findGCD(self, nums: List[int]) -> int:
        mn, mx = self.findMinMax(nums)
        gcd = 1

        for num in range(1,mn + 1):
            if mn%num == 0 and mx%num == 0:
                gcd = max(gcd, num)
        
        return gcd


        