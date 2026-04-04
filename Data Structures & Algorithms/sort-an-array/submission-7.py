class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            p = i 
            for j in range(i+1,n):
                if nums[j]<nums[p]:
                    p = j
            nums[i], nums[p] = nums[p], nums[i]
        return nums
        