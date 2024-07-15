class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        self.min_unfairness = float('inf')

        def bactrack(self, index, children):
            
            if index == len(cookies):
                self.min_unfairness = min(self.min_unfairness, max(children))
                return
            
            # the looping part
            for i in range(k):
                children[i] += cookies[index]
                if children[i] < self.min_unfairness:
                    bactrack(self,index + 1, children)
                children[i] -= cookies[index]
        
        bactrack(self,0, [0] * k)

        return self.min_unfairness