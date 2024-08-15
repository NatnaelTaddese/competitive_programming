class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        if difference == 0:
            count = Counter(arr)
            # return the max
            return max(val for key,val in count.items())

        n = len(arr)
        memo = defaultdict(int)

        answer = -1

        for i in arr:
            memo[i] = 1
            if memo[ i - difference] != 0:
                memo[i] += memo[i - difference]
            answer = max(answer, memo[i])
        
        return answer
