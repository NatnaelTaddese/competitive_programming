class Solution:
    def merge(self,list1, list2):
        i, j = 0, 0
        n, m = len(list1), len(list2)
        merged = [0 for _ in range(n + m)]
        k = 0
        while (i < n and j < m):
            if list1[i] < list2[j]:
                merged[k] = list1[i]
                i += 1
            else:
                merged[k] = list2[j]
                j += 1

            k += 1

        while (i < n):
            merged[k] = list1[i]
            i+=1
            k+=1
        
        while (j < m):
            merged[k] = list2[j]
            j+=1
            k+=1 
        
        return merged

    def mergeSort(self,nums):
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left,right)


    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
        