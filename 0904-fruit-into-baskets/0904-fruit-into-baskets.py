class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0
        right = 0

        seen = dict()

        max_fruits = 0

        while right < len(fruits):
            seen[fruits[right]] = seen.get(fruits[right], 0) + 1

            while len(seen) > 2:
                seen[fruits[left]] -= 1
                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)
            right += 1

        return max_fruits
