class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        str_nums = map(str, nums)
        # print(str_nums)

        str_nums = sorted(str_nums, key=LargerNumKey)

        largest_num = "".join(str_nums)
        return "0" if largest_num[0] == "0" else largest_num
