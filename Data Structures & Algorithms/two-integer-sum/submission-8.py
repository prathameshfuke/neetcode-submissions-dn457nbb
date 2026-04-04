class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapperhash = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in mapperhash:
                return [mapperhash[diff],i]
            mapperhash[n] = i
        return
            