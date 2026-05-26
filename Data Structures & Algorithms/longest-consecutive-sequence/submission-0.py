class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        nums_set = set(nums)
        for num in nums_set:
            if num-1 not in nums_set:
                currNum = num
                length = 1
                while currNum + 1 in nums_set:
                    length += 1
                    currNum += 1
                maxLen = max(maxLen, length)
        return maxLen