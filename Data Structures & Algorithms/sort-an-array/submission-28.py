class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums

        mid = len(nums)//2
        right = self.sortArray(nums[:mid])
        left = self.sortArray(nums[mid:])

        return self.mergesort(left,right)

    def mergesort(self,left,right):
        result, i,j = [],0,0

        while i <len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i = i+1
            else:
                result.append(right[j])
                j=j+1
        return result + left[i:] + right[j:]