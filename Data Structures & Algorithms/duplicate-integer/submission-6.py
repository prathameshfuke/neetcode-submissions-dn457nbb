class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        sortednum = sorted(nums)

        for n in sortednum:
            if n in seen:
                return True
            seen.add(n)
        return False
        