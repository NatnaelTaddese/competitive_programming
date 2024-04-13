class Solution(object):

    # Helper Functions

    def count_vowel_strings(self, words):
        vowels = set('aeiou')
        prefix_count = [0]
        for word in words:
            count = 0
            if word[0] in vowels and word[-1] in vowels:
                count = 1
            prefix_count.append(prefix_count[-1] + count)
        return prefix_count
    
    def count_queries(self, prefix_count, queries):
        ans = []
        for query in queries:
            left_count = prefix_count[query[0]]
            right_count = prefix_count[query[1] + 1]
            ans.append(right_count - left_count)
        return ans

    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        prefix_count = self.count_vowel_strings(words)
        return self.count_queries(prefix_count, queries)
            
        