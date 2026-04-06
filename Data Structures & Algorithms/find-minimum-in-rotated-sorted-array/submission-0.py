class Solution:
    def findMin(self, nums: List[int]) -> int:
        Min = float('inf')
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid]:
                Min = min(Min, nums[l])
                l = mid + 1
            else:
                Min = min(Min, nums[mid])
                r = mid - 1
        return Min


6, 7, 1, 2, 3, 4, 5