class Solution:
    def search(self, arr: List[int], target: int) -> int:
        
        arr.sort()

        left = 0
        right = len(arr)-1

        while left<=right:
            mid = (left + right)//2

            if arr[mid]<target:
                left = mid+1

            elif arr[mid]>target:
                right = mid - 1

            else:
                return mid
        return -1