class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        # return len(set(arr))
        mx = 1
        if not arr:
            return 0
        
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] > 1:
                arr[i] = arr[i - 1] + 1
                mx = arr[i]
            elif arr[i] - arr[i - 1] == 1:
                mx = arr[i]
        
        return mx

