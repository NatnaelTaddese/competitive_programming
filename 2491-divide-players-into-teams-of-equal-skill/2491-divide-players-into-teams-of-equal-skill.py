class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        

        left = 0
        right = len(skill) - 1

        shared_skill = skill[left] + skill[right] # 6
        # left += 1
        # right -= 1
        result = 0
        

        while(left <= right):
            temp = skill[left] + skill[right]
            if temp != shared_skill:
                return -1
            else:
                result += skill[left] * skill[right]
                left += 1
                right -= 1
        
        return result

        